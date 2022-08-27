# Import libraries
import json
import os.path
import time
import os
import socket

host = '0.0.0.0'
port = 7575



ServerSocket = socket.socket()
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print(f'Server is listing on the port {port}...')
ServerSocket.listen()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    with Client as connection:
        connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
        while True:
            data = connection.recv(2048)
            message = data.decode('utf-8')
            if message == 'BYE':
                break
            connection.sendall(str.encode(message))
        connection.close()