import os
os.mkdir("test")
read_file = open("folders.txt","r")

content_list = read_file.readlines()

for folder in content_list:
    os.mkdir("test/"+folder)