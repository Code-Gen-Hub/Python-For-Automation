# Mini Project 1: Auto Email Sender

# 1. Define Python Library
import smtplib
import ssl
from email.message import EmailMessage

# 2. Set function
def send_email(sender_email, receiver_email, subject, content, password):
  # Create email
  mail = EmailMessage() # activate library
  mail['To'] = receiver_email
  mail['Subject'] = subject
  mail['From'] = sender_email
  mail.set_content(content)

  # Set secure connection with email server - GMAIL
  secure_connect = ssl.create_default_context()

  # Connect to GMAIL server
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=secure_connect) as server:
    server.login(sender_email, password)
    server.send_message(mail)
    print('Email sent successfully!')

# 3. Main program
sender_email = 'example1.codegen@gmail.com'
password = 'nbujmcnefkjsafyu'
receiver_email = input('Recipient email address: ')
subject = input('Email Subject: ')
content = input('Email Message: ')

send_email(sender_email, receiver_email, subject, content, password)
