from socket import *


myName = input("이름 입력: ")
port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

while True:
    sendData = (myName + ": "+ input("나 : "))
    connectionSock.send(sendData.encode('utf-8'))

    recvData = connectionSock.recv(1024)
    print(recvData.decode('utf-8'))
