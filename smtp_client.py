#! /usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from getpass import getpass

# Email configuration
sender_email = input("Enter your email address: ")
receiver_email = input("Enter recipient's email address: ")
password = getpass("Enter your email password: ") # Securely input password
subject = "Test Email from DS"
body = "Hello! This is a test email sent using Python's smtplib."
server = None

# Create MIMEText object for email content
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

# Connect to SMTP server
try:
   # Using Gmail's SMTP server (use smtp.gmail.com for Gmail)
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls() # Enable TLS encryption
   server.login(sender_email, password) # Authenticate
   server.sendmail(sender_email, receiver_email, msg.as_string()) # Send email
   print("Email sent successfully!")

except smtplib.SMTPAuthenticationError:
   print("Error: Authentication failed. Check your email and password.")

except smtplib.SMTPException as e:
   print(f"SMTP error occurred: {e}")

except Exception as e:
   print(f"Error: {e}")

finally:
   if server:
      server.quit() # Close the connection
