import smtplib
import os

sender = "akil.dove@gmail.com"
receiver = "akilan.468@gmail.com"

user_name = "akil.dove@gmail.com"
password = os.getenv("GMAIL_PASSWORD")

message = f"""\
Subject: Email From Python
To: {receiver}
From: {sender}
Hi This is from Python!!!!"""

print(message)

with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
    server.login(user_name,password)
    server.sendmail(sender,receiver,message)
    print("Successfully Sent")