from socket import *
import sys # In order to terminate the program


input = (sys.argv)
server_host = input[1]
server_port = input[2]
filename = input[3]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server_host, server_port))
    s.sendall('GET /' + filename + ' HTTP1.1\r\n\r\n')
    data = s.recv(1024)
print('Received', repr(data))