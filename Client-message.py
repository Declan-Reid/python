#!/usr/bin/env python3
import sys
import socket
from threading import *
import errno

IP = ''
PORT = int()

HEADER_LENGTH = 10
try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
except IndexError:
    while (IP == '') or (PORT == int()):
        try:
            IP = input('IP: ')
            PORT = int(input('Port: '))
        except:
            IP = ''
            PORT = int()
my_username = input("Username: ")

# Create a socket
# socket.AF_INET - address family, IPv4, some other possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won't block, just return some exception we'll handle
client_socket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    # Wait for user to input a message
    message = input(str(my_username)+' > ')
    print()

    if message.replace(str(my_username)+' > ', '') == '':
        print("\033[F\033[F")

    else:

        # If message is not empty - send it
        if message:

            # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)