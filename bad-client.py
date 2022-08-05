import socket
import sys

try:
    host = sys.argv[1]
    port = int(sys.argv[2])
except IndexError:
    host = input('IP: ')
    port = input('Port: ')

username = input('Username: ')

ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
Response = ClientSocket.recv(2048)
while True:
    Input = input(str(username)+'> ')
    print('\033[F')
    ClientSocket.send(str.encode(str(username)+'> '+Input))
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))
ClientSocket.close()

import sys
import socket 
import threading

username = input('Username : ')

class ClientNode:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = sys.argv[1]
        port = int(sys.argv[2])
        ip_and_port = (ip, port)
        self.node.connect(ip_and_port)

    def send_sms(self, SMS):
        self.node.send(SMS.encode())
        print("\033[F"+SMS)

    def receive_sms(self):
        while True:       
            data = self.node.recv(1024).decode()
            if data != '':
                print(data)

    def main(self):
        while True:
            messageTmp = input()
            message=username+' > '+messageTmp
            self.send_sms(message)

while True:
    Client = ClientNode()
    always_receive = threading.Thread(target=Client.receive_sms)
    always_receive.daemon = True
    always_receive.start()
    Client.main()