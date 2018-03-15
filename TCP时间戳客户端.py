#coding=utf-8

from socket import *

HOST = '118.89.248.99' #  or 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR=(HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)#创建套接字
tcpCliSock.connect(ADDR)#连接服务器

while True:#通讯循环
    data = input('> ')#从键盘得到数据
    #print('data=',data);
    if not data:#如果只输入enter不带任何数据，则中断循环
        break
    tcpCliSock.send(data.encode())#将从键盘得到的数据编码成字节流数据，发送到服务器端
    data = tcpCliSock.recv(BUFSIZ).decode()#将从服务器端得到的字节流数据还原成字符串
    if not data:#服务器关闭中断循环
        break
    print(data)

tcpCliSock.close()#关闭连接
