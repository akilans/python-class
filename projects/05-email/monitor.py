import requests
from email_agent import send_mail
import time

websites = ["http://localhost:7000","http://localhost:8000"]

while True:
    for website in websites:
        try:
            response = requests.get(website)
            if response.status_code != 200:
                print(website+" - Website is Down!!!")
                #send_mail(website+" - Website is Down!!!")
                time.sleep(60)
            else:
                print(website+" - Website is up!!!")
        except requests.exceptions.ConnectionError:
            print(website+" - Website down!!!")
            #send_mail(website+" - Website is Down!!!")
            time.sleep(60)

    time.sleep(10)
        