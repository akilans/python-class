from bs4 import BeautifulSoup
import requests

laptop_data = open("laptop.txt","w")

html_page = requests.get("https://gadgets.ndtv.com/laptops")
html_content = BeautifulSoup(html_page.text,"lxml")

#print(html_content)

#print(html_content.title.text)
laptop = html_content.find("div",class_="thumb")
laptops = html_content.find_all("div",class_="thumb")
#print(laptops)
for laptop in laptops:

    if laptop.picture:
        #print(laptop.picture.img["alt"])
        laptop_data.write(laptop.picture.img["alt"])
    elif laptop.img:
        #print(laptop.img["alt"])
        laptop_data.write(laptop.img["alt"])
    laptop_data.write("\n")
laptop_data.close()
