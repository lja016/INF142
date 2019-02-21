from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start


serverSocket.bind(('localhost', 80))
serverSocket.listen(1)


#Fill in end


while True:
    #Establish the connection
    print('Ready to serve...')
    
    #Fill in start
    connectionSocket, addr = serverSocket.accept()
    #Fill in end          
    try:
        #Fill in start 
        message = connectionSocket.recv(1024).decode()
        #Fill in end      
        filename = message.split()[1]                 
        f = open(filename[1:])
        
        #Fill in start  
        outputdata = f.read()
        f.close

        #Fill in end   
        
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        #Fill in end
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send('HTTP/1.1 404 Not Found\n'.encode())
        #Fill in end
        #Close client socket
        #Fill in start
        #Fill in end
connectionSocket.close()

sys.exit() #Terminate the program after sending the corresponding data                                    






