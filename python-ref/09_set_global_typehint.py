balance = 0

# set has unique values -no duplicates
def demo_set():
    
    friends = [
        {"name": "Alex","location":"Tenkasi"},
        {"name": "Kumar","location":"Tenkasi"},
        {"name": "Jegan","location":"Tenkasi"},
        {"name": "Kathir","location":"Coimbatore"},
        {"name": "Karuna","location":"Hyderabad"},
    ]

    locations = set()
    for friend in friends:
        locations.add(friend["location"])
    print(locations) # {'Hyderabad', 'Coimbatore', 'Tenkasi'}


# demo global
def demo_global():
    deposit(100)
    print(balance) # 100
    withdraw(50)
    print(balance) # 50

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

def demo_typehint():
    my_name: str = "Akilan"
    my_age: int = 35
    friends: list = ["Alex","Kumar","Jegan"]

    print_friends(friends)
    msg = about_me(my_name,my_age)
    print(msg)

# function with type hint
def print_friends(friends: list) -> None:
    for friend in friends:
        print(friend)
# function with type hint and return value
def about_me(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"


def main():
    #demo_set()
    #demo_global()
    '''
    pip install mypy
    mypy 09_etc.py
    '''
    demo_typehint() 


if __name__ == "__main__":
    main()