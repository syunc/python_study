#coding = utf-8
from socket import * #调用socket中的所有模块
from time import ctime#调用ctime模块

HOST = ''#这是对bind()方法的标识，表示可以使用任何可以使用的地址
PORT = 21567#端口号
BUFSIZ = 1024#缓冲区大小
ADDR = (HOST,PORT)#地址


udpSerSock = socket(AF_INET,SOCK_DGRAM)#创建套接字
udpSerSock.bind(ADDR)#等待连接

while True:
    print("waiting for message...")
    data , addr = udpSerSock.recvfrom(BUFSIZ)#返回的是一个元组类型，一个套接字和地址
    #所以data得到的是数据，addr得到的是地址
    data = data.decode()#数据报编码还原成字符串
    print("data=",data)
    udpSerSock.sendto(('[%s] %s'%(ctime(),data)).encode(),addr)#将要发送的数据编码成数据报，发送至addr
    print("received from and return to :",addr)#addr为客户端的ip和端口号
udpSerSock.close()
