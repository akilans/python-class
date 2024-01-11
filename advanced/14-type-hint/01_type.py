# Type hint example
# str,int,float -Primitive data type
# list,set,tuple,dict - Non -Primitive data type
# pass class type
class Person:
    def __init__(self,name):
        self.name = name

def greet(name: str) -> str:
    """
    Function to greet user with uppercase
    Parameters:
        name: str - Name of the user
    Return:
        msg: str -> return greet message with uppercase of username
    """
    return f"Hello, {name.upper()} !!!"

# pass str, int, float -> Default case, either or choice
def say_my_details(name: str,age: int, height: float | int = 0.0) -> str:
    return f"Your name is {name}. You're {age} years old with height of {height}"

# pass list data type
def print_friends(friends: list[str]) -> None:
    for friend in friends:
        print(friend)

# pass class data type
def print_person_details(p: Person) -> None:
    print(p.name)

# pass dict
def print_dict(friends: dict[str, str]) -> None:
    for name,location in friends.items():
        print(f"{name} ---> {location}")

def main():
    user_name: str = "Akilan"
    msg: str = greet(user_name)
    print(msg)

    user_age: int = 35
    user_height: float = 5.7

    details = say_my_details(user_name,user_age,user_height)
    print(details)
    inba_details = say_my_details("Inba",5)
    print(inba_details)

    print_friends(["Alex","Jegan","Kumar"])


    user_details = Person(user_name)
    print_person_details(user_details)

    friends_details = {
        "Alex": "Tenkasi",
        "Kumar": "Tenkasi",
        "Kathir": "Erode"
    }
    print_dict(friends_details)
    

if __name__ == "__main__":
    main()

'''
pip install mypy
mypy 01_type.py --check-untyped-defs
output:
Hello, AKILAN !!!
Your name is Akilan. You're 35 years old with height of 5.7
Your name is Inba. You're 5 years old with height of 0.0
Alex
Jegan
Kumar
Akilan
Alex ---> Tenkasi
Kumar ---> Tenkasi
'''