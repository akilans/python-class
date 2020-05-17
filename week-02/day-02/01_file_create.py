
filename = "C:/Users/akilan_s/Desktop/friends.txt"

# Write file
durga_file = open(filename,"w") # w -write mode, a - append mode, r - read mode
durga_file.write("File for Durga \n")
durga_file.write("It is secure \n")
durga_file.close()

# Append data
durga_file = open(filename,"a") # w -write mode, a - append mode, r - read mode
durga_file.write("File for Akilan \n")
durga_file.write("It is also secure \n")
durga_file.close()

# Read data
durga_file = open(filename,"r") # w -write mode, a - append mode, r - read mode
content = durga_file.read()
print(content)
durga_file.close()

# Read data with necessary characters
durga_file = open(filename,"r") # w -write mode, a - append mode, r - read mode
content = durga_file.read(5)
print(content)
durga_file.close()

# Read data by one line
durga_file = open(filename,"r") # w -write mode, a - append mode, r - read mode
content = durga_file.readline()
print(content)
durga_file.close()

# Read data by all lines
durga_file = open(filename,"r") # w -write mode, a - append mode, r - read mode
content = durga_file.readlines()
print("Second line - " + content[1])
print(content)
durga_file.close()
