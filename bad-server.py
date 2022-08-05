import socket 
from _thread import *

# Define host and port
host = '127.0.0.1'
port = 12888

def client_handler(connection):
    connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
    while True:
        data = connection.recv(2048)
        message = data.decode('utf-8')
        if message == 'BYE':
            break
        connection.sendall(str.encode(message))
    connection.close()

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, ))

def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Server is listing on the port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)
start_server(host, port)



username = input('Username : ')

class ServerNode:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12888)
        self.node.bind(port_and_ip)
        self.node.listen(5)
        self.connection, addr = self.node.accept()

    def accept_connections(ServerSocket):
        Client, address = ServerSocket.accept()
        print(f'Connected to: {address[0]}:{str(address[1])}')
        threading.Thread(target=server.main) 

    def send_sms(self, SMS):
        self.connection.send(SMS.encode())
        print("\033[F"+SMS)

    def receive_sms(self):
        while True:
            data = self.connection.recv(1024).decode()
            if data == '':
                break
            print(data)

    def main(self):
        while True:
            messageTmp = input()
            message=username+' > '+messageTmp
            self.send_sms(message)

server = ServerNode()
always_receive = threading.Thread(target=server.receive_sms)
always_receive.daemon = True
always_receive.start()
while True:
        server.accept_connections(socket.socket)
server.main()