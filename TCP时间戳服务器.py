#coding=utf-8
#创建TCP服务器
from socket import *
from time import ctime

HOST=''
PORT=21567#端口号
BUFSIZ=1024#缓冲区大小
ADDR=(HOST,PORT)#地址

tcpSerSock=socket(AF_INET,SOCK_STREAM) #创服务器套接字
tcpSerSock.bind(ADDR) #套接字与地址绑定
tcpSerSock.listen(5)  #监听连接,传入连接请求的最大数

while True:
    print('waiting for connection...')
    tcpCliSock,addr =tcpSerSock.accept()#等待客户端发送消息
    print('...connected from:',addr)

    while True:
        data =tcpCliSock.recv(BUFSIZ).decode()#接受来自客户端的字符串
        #由于客户端发送来的为字节流所以用decode()编码成字符串
        #在通信的过程中TCP消息只能为字节流或UDP的数据报
        print('date=',data)
        if not data:
            break
        tcpCliSock.send(('[%s] %s' %(ctime(),data)).encode())#将要发送的数据编码成字节流回送客户端

    tcpCliSock.close()#客户端关闭
tcpSerSock.close()#服务器端关闭，理论上不存在
