#! /usr/bin/python3

import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen()
print("Server will start listening to port 12345...")
while(True):
   conn, addr = server_socket.accept()
   print(f"Connection established with {addr}")
   conn.sendall("Hello from server!\n".encode())
   conn.sendall(f"Your current IP address is {addr[0]}.\n".encode())
   conn.sendall(f"Your client's port is {addr[1]}.".encode())

# alternatives:
#conn.sendall("Hello from server!".encode('utf-8'))
#conn.sendall(b"Hello from server!")
#conn.close()