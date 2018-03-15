#coding = utf-8
from socket import *
from time import ctime

HOST = '118.89.248.99'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)


udpCliSock = socket(AF_INET,SOCK_DGRAM)


while True:
    data = input('>')
    
    if not data:
        break
    udpCliSock.sendto(data.encode(),ADDR)
    data,addr = udpCliSock.recvfrom(BUFSIZ)
    print(data.decode())
udpCliSock.close()
