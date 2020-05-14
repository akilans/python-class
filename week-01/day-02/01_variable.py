# Variable session
# Types - String, Integer, Float, List, Tuples, Dictionary

# string
name = "Durga" 
print(type(name))
print(name)

# Int
age = 35 
print(type(age))
print(age)

# Float
height = 5.8 
print(type(height))
print(height)

# List
friends = ["Akilan", "Gopal", "Anurock"] 
print(type(friends))
friends.append("Siva") # Add data to list
print(friends)
print(len(friends))
print(friends[2])

# Tuples
coordinates = (2,5) 
print(coordinates[1])

# Dictionary
employee = { 
    "akilan": {
        "name": "Akilan",
        "company": "Infosys",
        "location": "United Kingdom"
    },
    "gopal": {
        "name": "Gopal",
        "company": "IBM",
        "location": "India"
    }
}

print(type(employee))
print(employee)
print(employee["akilan"])
print(employee["gopal"]["company"])

