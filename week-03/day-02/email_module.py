import smtplib
import os

sender = "akil.dove@gmail.com"
receiver = "akilan.468@gmail.com"

message = f"""\
Subject: Email From Python
To: {receiver}
From: {sender}
CPU usgae exceeded"""

user_name = "akil.dove@gmail.com"
password = os.getenv("GMAIL_PASSWORD")

def send_email_function():
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(user_name,password)
        server.sendmail(sender,receiver,message)
        print("Successfully Sent")