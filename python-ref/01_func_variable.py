# main function
def main():
    hello()
    name = input("What's your name? ").strip().upper()
    hello(name)
    x = int(input("Enter x: "))
    print(f"Square value of {x} is {square(x)}")

# function with return value
def square(n):
    return n * n

# function without return value
def hello(to="World"):
    print("Hello,",to)
    print(f"Hello, {to}")
    print("DevOps","Docker","Kubernetes","AWS","Python",sep="|",end="\n")

# List operations
def list_operations():
    friends = []
    friends.append("Alex")
    friends.extend(["Jegan","Kumar"])

    for friend in friends:
        print(friend)

    friends_copy = friends # pointing to the same address, deep copy
    friends_copy.append("Mathan")
    print(friends) # ['Alex', 'Jegan', 'Kumar', 'Mathan']
    print(friends_copy) # ['Alex', 'Jegan', 'Kumar', 'Mathan']

    friends.remove("Mathan")
    print(friends) # ['Alex', 'Jegan', 'Kumar']

    old_friends = friends.copy() # best way to copy - shallow copy
    old_friends.append("Mathan")
    print(old_friends) # ['Alex', 'Jegan', 'Kumar', 'Mathan']
    print(friends) #['Alex', 'Jegan', 'Kumar']

    old_friends.clear() # clear all data
    print(old_friends) #[]

    new_friends = ["Gayatri","Karuna"]
    all_friends = friends + new_friends
    print(all_friends) # ['Alex', 'Jegan', 'Kumar', 'Gayatri', 'Karuna']


# Dict operation
def dict_operations():
    my_details = {}
    my_details["name"] = "Akilan"
    my_details["location"] = "Tenkasi"
    my_details["age"] = 35

    print(my_details) # {'name': 'Akilan', 'location': 'Tenkasi', 'age': 35}

    print(my_details.keys()) # dict_keys(['name', 'location', 'age'])
    print(my_details.values()) # dict_values(['Akilan', 'Tenkasi', 35])

    for k,v in my_details.items():
        print(f"{k} ----> {v}")
        '''
            name ----> Akilan
            location ----> Tenkasi
            age ----> 35
        '''

    my_another_details = {"role": "Principal Devops Engineer"}
    all_details = {**my_details,**my_another_details}
    print(all_details) # {'name': 'Akilan', 'location': 'Tenkasi', 'age': 35, 'role': 'Principal Devops Engineer'}
    my_another_details.clear()
    print(my_another_details) # {}


# it will get executed only when call the script directly
# if we import into other script it will not get executed
# python 01_func_variable.py
if __name__ == "__main__":
    main()
    #list_operations()
    #dict_operations()


'''
Output:
Hello, World
Hello, World
DevOps|Docker|Kubernetes|AWS|Python
What's your name? Akilan
Hello, AKILAN
Hello, AKILAN
DevOps|Docker|Kubernetes|AWS|Python
Enter x: 5
Square value of 5 is 25
'''