#! /usr/bin/python3

import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))
message = client_socket.recv(1024)
print("Message from server:", message.decode())
client_socket.close()
