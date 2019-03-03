from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverSocket.bind(('', 8000))
serverSocket.listen()

while True:
    
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
        
        #Receive the request from socket
        message = connectionSocket.recv(1024).decode()
        
        #Check for empty requests (Google Chrome apparently does this :< )
        if len(message) > 0:
            filename = message.split()[1]                 
            f = open(filename[1:]) 
            outputdata = f.read()
            f.close
            
            #Send one HTTP header line into socket
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):           
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            
        connectionSocket.close()
    except IOError:
        
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n<!DOCTYPE html><html><head><meta charset="utf-8"><title>404 page not found</title></head><body><h1>404 nothing too see here</h1></body></html>'.encode())
        connectionSocket.close()
connectionSocket.close()
sys.exit() #Terminate the program after sending the corresponding data