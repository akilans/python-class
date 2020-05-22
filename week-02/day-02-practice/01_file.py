filename = "akilan.txt"
'''
# Modes - Write, Read, Append
sample_file = open(filename,"w")
sample_file.write("Hi This is Akilan \n")
sample_file.write("I am in UK \n")
sample_file.close()
'''
'''
# Append mode
# Modes - Write, Read, Append
append_file = open(filename,"a")
append_file.write("\nI am DevOps Engineer\t in BP")
append_file.write("\nI Like python")
append_file.close()
'''
'''
# Read
read_file = open(filename,"r")
content = read_file.read()
read_file.close()
print(content)
'''
# Read by line
read_file_by_lines = open(filename,"r")
content = read_file_by_lines.readlines()
#print(content)
read_file_by_lines.close()
print(content[1])

