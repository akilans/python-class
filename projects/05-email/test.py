import smtplib
import os


# Specify the sender’s and receiver’s email addresses:
sender = "from@example.com"
receiver = "mailtrap@example.com"

# Type your message: use two newlines (\n) to separate the subject from the message body, and use 'f' to  automatically insert variables in the text
message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}
This is my first message with Python."""

print(message)

'''

login = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(login, password)
    server.sendmail(sender, receiver, message)
'''