filename = input("Enter file name : ")

write_file = open(filename,"w")

file_content = ""

while file_content != "quit":
    file_content = input("Enter file content: ")
    if file_content != "quit":    
        write_file.write(file_content+"\n")

write_file.close()