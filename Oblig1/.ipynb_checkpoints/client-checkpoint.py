from socket import *
import sys # In order to terminate the program

clientSocket = socket(AF_INET, SOCK_STREAM)

input = (sys.argv)
server_host = input[1]
server_port = input[2]
filename = input[3]