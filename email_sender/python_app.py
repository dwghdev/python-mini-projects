# Go over to our gmail account and setup 2 way factor authentication
# Generate app password
# Create a function to send the mail

from email.message import EmailMessage
from secret_email_password import secret
import ssl
import smtplib

email_sender = 'dalewaltergh@gmail.com'
email_password = secret

email_receiver = 'dale@proudcloud.io'
subject = 'Email received!'
body = """
    This is a sample message body
"""

email_message = EmailMessage()
email_message['From'] = email_sender
email_message['To'] = email_receiver
email_message['Subject'] = subject
email_message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email_message.as_string())
