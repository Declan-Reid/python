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

    def receive_sms(self):
        while True:       
            data = self.node.recv(1024).decode()
            print(data)

    def main(self):
        while True:
            messageTmp = input()
            message=username+' > '+messageTmp
            self.send_sms(message)

Client = ClientNode()
always_receive = threading.Thread(target=Client.receive_sms)
always_receive.daemon = True
always_receive.start()
Client.main()