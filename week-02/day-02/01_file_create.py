
filename = "./test/friends.txt"

# Write file
# w -write mode, a - append mode, r - read mode
durga_file = open(filename, "w")
durga_file.write("File for Durga \n")
durga_file.write("It is secure \n")
durga_file.close()

# Append data
# w -write mode, a - append mode, r - read mode
durga_file = open(filename, "a")
durga_file.write("File for Akilan \n")
durga_file.write("It is also secure \n")
durga_file.close()

# Read data
# w -write mode, a - append mode, r - read mode
durga_file = open(filename, "r")
content = durga_file.read()
print(content)
durga_file.close()

# Read data with necessary characters
# w -write mode, a - append mode, r - read mode
durga_file = open(filename, "r")
content = durga_file.read(5)
print(content)
durga_file.close()

# Read data by one line
# w -write mode, a - append mode, r - read mode
durga_file = open(filename, "r")
content = durga_file.readline()
print(content)
durga_file.close()

# Read data by all lines
# w -write mode, a - append mode, r - read mode
durga_file = open(filename, "r")
content = durga_file.readlines()
print("Second line - " + content[1])
print(content)
durga_file.close()
