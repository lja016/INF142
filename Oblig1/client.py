from socket import *
import sys # In order to terminate the program


input = (sys.argv)
server_host = input[1]
server_port = int(input[2])
filename = input[3]



client_socket = socket(AF_INET, SOCK_STREAM)
server_address = (server_host, server_port)
client_socket.connect(server_address)

request_header = ('GET /' + filename + ' HTTP1.1\r\n\r\n')
client_socket.send(request_header.encode())

response = ''
while True:
    recv = client_socket.recv(1024).decode()
    if not recv:
        break
    response += recv 

print(response)
client_socket.close()    