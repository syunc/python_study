#coding = utf-8
from socket import * #����socket�е�����ģ��
from time import ctime#����ctimeģ��

HOST = ''#���Ƕ�bind()�����ı�ʶ����ʾ����ʹ���κο���ʹ�õĵ�ַ
PORT = 21567#�˿ں�
BUFSIZ = 1024#��������С
ADDR = (HOST,PORT)#��ַ


udpSerSock = socket(AF_INET,SOCK_DGRAM)#�����׽���
udpSerSock.bind(ADDR)#�ȴ�����

while True:
    print("waiting for message...")
    data , addr = udpSerSock.recvfrom(BUFSIZ)#���ص���һ��Ԫ�����ͣ�һ���׽��ֺ͵�ַ
    #����data�õ��������ݣ�addr�õ����ǵ�ַ
    data = data.decode()#���ݱ����뻹ԭ���ַ���
    print("data=",data)
    udpSerSock.sendto(('[%s] %s'%(ctime(),data)).encode(),addr)#��Ҫ���͵����ݱ�������ݱ���������addr
    print("received from and return to :",addr)#addrΪ�ͻ��˵�ip�Ͷ˿ں�
udpSerSock.close()
