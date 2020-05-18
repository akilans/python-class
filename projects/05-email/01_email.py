import smtplib
import os
from email.message import EmailMessage
import imghdr

msg = EmailMessage()
msg["From"] = "cpu.memory.disk@gmail.com"
msg["to"] = "akil.dove@gmail.com"
msg["Subject"] = "Test Email"
msg.set_content("This is test email from Python. Image attached")

image_list = ["lion-1.jpg","lion-2.jpg"]

for file in image_list:
    with open(file,"rb") as imagefile:
        file_data = imagefile.read()
        file_type = imghdr.what(imagefile.name)
        file_name = imagefile.name

    msg.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(EMAIL,PASSWORD)
    smtp.send_message(msg)