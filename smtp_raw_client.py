#! /usr/bin/python3

import socket
import ssl
from getpass import getpass
# Email configuration
sender_email = input("Enter your email address: ")
receiver_email = input("Enter recipient's email address: ")
password = getpass("Enter your email password: ") # Securely input password
smtp_server = "smtp.gmail.com"
port = 587
sock = None
# Create socket
try:
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect((smtp_server, port))
   print("Connected to SMTP server")

   # Receive server greeting
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

   # Send EHLO
   sock.send("EHLO localhost\r\n".encode())
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

   # Start TLS
   sock.send("STARTTLS\r\n".encode())
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

   # Wrap socket with TLS
   context = ssl.create_default_context ()
   sock = context.wrap_socket(sock , server_hostname = smtp_server)
   print ("TLS handshake completed ")

   # Send EHLO again after STARTTLS
   sock.send("EHLO localhost\r\n".encode())
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

   # Authenticate (simplified BASE64 encoding for demo)
   import base64
   sock.send("AUTH LOGIN\r\n".encode())
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

   sock.send(base64.b64encode(sender_email.encode()) + b"\r\n")
   response = sock.recv(1024).decode()
   print(f"Server: {response}")
   
   sock.send(base64.b64encode(password.encode()) + b"\r\n")
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

   # Send email
   sock.send(f"MAIL FROM:<{sender_email}>\r\n".encode())
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

   sock.send(f"RCPT TO:<{receiver_email}>\r\n".encode())
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

   sock.send("DATA\r\n".encode())
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

   # Email content
   email_content = (
      f"From: {sender_email}\r\n"
      f"To: {receiver_email}\r\n"
      f"Subject: Test Email from DS Raw Sockets\r\n"
      f"\r\n"
      f"Hello! This is a test email sent using raw sockets in Python.\r\n"
      f".\r\n"
   )
   sock.send(email_content.encode())
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

   # Quit
   sock.send("QUIT\r\n".encode())
   response = sock.recv(1024).decode()
   print(f"Server: {response}")

except socket.error as e:
   print(f"Socket error: {e}")

except Exception as e:
   print(f"Error: {e}")

finally:
   if sock:
      sock.close()
      print("Socket closed")
