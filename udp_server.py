from socket import *
serverPort = 9999
serverName = 'localhost'
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))#To accept connection with client we pass localhost and serverport which is free
print("The server is ready to recieve")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)