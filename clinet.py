from socket import *

myName = input("이름 입력: ")


port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('접속 완료')

while True:
    recvData = clientSock.recv(1024)
    print(recvData.decode('utf-8'))

     sendData = (myName + ": "+ input("나 : "))
    clientSock.send(sendData.encode('utf-8'))
