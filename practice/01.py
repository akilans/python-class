print("Hello")
# Hello
name = "Akilan"

print(f"Hello {name}, keep rocking")
# Hello Akilan, keep rocking

greetings = "Welcome to python"

greet_list = greetings.split(" ")
print(greet_list)  # ['Welcome', 'to', 'python']

# reverse string
print(greetings[::-1])
# nohtyp ot emocleW

for i in range(5):
    print(i)
'''
0
1
2
3
4
'''

friends = ["Alex", "Jegan", "Kumar"]

for friend in friends:
    print(friend)
'''
Alex
Jegan
Kumar
'''
# add new friend
friends.append("kathir")
print(friends)
# ['Alex', 'Jegan', 'Kumar', 'kathir']
friends_details = {
    "akilan": {
        "location": "Bangalore",
        "age": 34
    },
    "alex": {
        "location": "Bangalore",
        "age": 35
    },
    "kumar": {
        "location": "Chennai",
        "age": 34
    }
}


print("Akilan location %s and age is %d" %
      (friends_details["akilan"]["location"], friends_details["akilan"]["age"]))
# Akilan location Bangalore and age is 34

# loop dictionary
for fnd in friends_details:
    print(friends_details[fnd])

'''
{'location': 'Bangalore', 'age': 34}
{'location': 'Bangalore', 'age': 35}
{'location': 'Chennai', 'age': 34}s
'''
for key, value in friends_details.items():
    print(f"{key} - {value}")

'''
akilan - {'location': 'Bangalore', 'age': 34}
alex - {'location': 'Bangalore', 'age': 35}
kumar - {'location': 'Chennai', 'age': 34}
'''
# if else
if name == "Akilan":
    print("He is great")
elif name == "Alex":
    print("Alex too")
else:
    print("Not sure")
