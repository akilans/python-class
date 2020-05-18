import smtplib
import os
from email.message import EmailMessage
import imghdr

def send_mail(error_msg):

    msg = EmailMessage()
    msg["From"] = "cpu.memory.disk@gmail.com"
    msg["to"] = "akilan.devops@gmail.com"
    msg["Subject"] = "CPU/Memory/Disk Alert!!!"
    msg.add_alternative("""\n
    <html>
    <head></head>
    <body>
    <div>"""+error_msg+"""</div>
    </body>
    </html>
    """,subtype="html")


    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(EMAIL,PASSWORD)
        smtp.send_message(msg)
