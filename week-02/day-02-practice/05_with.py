'''
read_file = open("akilan.txt","r")
content = read_file.read()
print(content)
read_file.close()
'''
with open("akilan.txt","r") as read_file:
    content = read_file.read()
    print(content)