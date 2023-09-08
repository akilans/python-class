# create and write into a file
with open("hello.txt", "w") as myfile:
    myfile.write("Hello Akilan\n")


with open("hello.txt", "a") as myfile:
    myfile.write("Hello Inba\n")

with open("hello.txt", "r") as myfile:
    print(myfile.read())


with open("hello.txt", "r") as myfile:
    print(myfile.readline())
