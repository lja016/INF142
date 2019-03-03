from socket import *
import sys # In order to terminate the program


input = (sys.argv)
server_host = input[1]
server_port = int(input[2])
filename = input[3]



client_socket = socket(AF_INET, SOCK_STREAM)
server_address = (server_host, server_port)
client_socket.connect(server_address)

#creating the GET request header
request_header = ('GET /' + filename + ' HTTP1.1\r\n\r\n')

#send the header into the socket
client_socket.send(request_header.encode())

response = ''
while True:
	#receive a response message from the socket
    recv = client_socket.recv(1024).decode()
    if not recv:
        break
    response += recv 

print(response)
client_socket.close()    