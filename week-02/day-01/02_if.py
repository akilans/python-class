
name = input("Enter name : ")
age = input("Enter age : ")

if name == "durga" or name == "gopi" or name == "akilan":
    print(" User "+ name + " found")
    print("user found")

# name = name.lower()
# print(name)

#if name is equal to durga then print matched

# Nested if condition
if name == "durga":
    if age == "35":
        print("Found correct durga")
    else:
        print("duplicate durga")
        print("ajkshdagdjkad")
elif name == "gopi": # else if / elif
    print("Gopi found")
elif name == "akilan":
    print("akilan found")
else:
    print("Name not matched")
print("Done............")