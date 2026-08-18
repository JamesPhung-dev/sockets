#! /usr/bin/python3

import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen()
print("Server is listening on port 12345...")
conn, addr = server_socket.accept()
print(f"Connection established with {addr}")
conn.sendall("Hello from server!".encode())
# alternatives:
#conn.sendall("Hello from server!".encode('utf-8'))
#conn.sendall(b"Hello from server!")
conn.close()
