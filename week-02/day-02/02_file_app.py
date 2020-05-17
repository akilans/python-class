filename = input("Enter the file name : ")

user_file = open(filename,"w")


content = ""

while content != "quit":
    content = input("Enter the content : ")
    if content == "quit":
        break
    user_file.write(content+"\n")

user_file.close()
print("File saved successfully")

user_file = open(filename,"r")
file_content = user_file.read()
print(file_content)
user_file.close()
