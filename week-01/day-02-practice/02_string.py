first_name = "Durga"
last_name = "Kata"
age = 35

friends = ["Akilan","Durga","Akilan"]
print(list(set(friends))) 

# + used to join 2 strings
full_name = first_name + " "+ last_name
print(len(first_name))
print(first_name[0])

print(first_name[0:3])

entire_name = "Akilan,Inba,Subramanian"
name_list = entire_name.split(",")
print(name_list)
print("AKI - First name is "+ name_list[0])
print("AKI - Middle name is "+ name_list[1])
print("AKI - Last name is "+ name_list[2])

print(full_name)
print("Full name is "+ first_name+" " + last_name +" his age is "+ str(age)) # Type casting