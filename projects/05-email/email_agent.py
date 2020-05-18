import smtplib
import os
from email.message import EmailMessage
import imghdr

def send_mail(error_msg):

    msg = EmailMessage()
    msg["From"] = "24/7 - Monitoring"
    msg["to"] = "akil.dove@gmail.com"
    msg["Subject"] = "Critical Error!!!"
    msg.add_alternative("""\n
    <html>
    <head></head>
    <body>
    <h1>"""+error_msg+"""</h1>
    </body>
    </html>
    """,subtype="html")


    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(EMAIL,PASSWORD)
        smtp.send_message(msg)
