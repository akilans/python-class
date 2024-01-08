class Person:
    # class variable
    default_greet = "Welome to Python oops"

    # constructor
    def __init__(self,name):
        self.name = name # this will call setter

    #getter
    @property
    def name(self):
        return self._name # self.name -> calls getter -> So it will infinite loop
    
    #setter
    @name.setter
    def name(self,name):
        if len(name) < 2:
            raise ValueError("Invalid name")
        self._name = name # self.name -> calls setter -> So it will infinite loop

    #print class
    def __str__(self):
        return f"Person name is {self.name}" # {self.name} this will call getter
    
    # normal method
    def greet(self):
        return f"Hello {self.name}, Welcome to oops..." # {self.name} this will call getter

    
    #class method
    @classmethod
    def greet_class(cls,name):
        return f"Hello {name} {cls.default_greet}"
    
    # operator overloading -> +,-,*,>,<,==, etc
    def __add__(self,other):
        return f"{self.name} & {other.name}"


# child class - inheritence example
class Friend(Person):
    # constructor
    def __init__(self, name,type):
        super().__init__(name) # use parent constructor with getter and setter
        self.type = type
    # overwrite parent method
    def __str__(self):
        return f"{self.name} is my {self.type} friend"
    
# create object from class
per1 = Person("Alex")

print(per1)
print(per1.greet())

# try and except to validate setter
try:
    per1.name = "A"
except ValueError:
    print("Error happened")

# call class method without creating an object
print(Person.greet_class("Akilan"))

#add 2 objects
per2 = Person("Kumar")
print(per1 + per2)


friend1 = Friend("Annachi","School")
friend2 = Friend("Karuna","Office")
print(friend1)
print(friend2)
try:
    friend3 = Friend("B","college")
except ValueError:
    print("Error happened")
'''
Output:
Person name is Alex
Hello Alex, Welcome to oops...
Error happened
Hello Akilan Welome to Python oops
Alex & Kumar
Annachi is my School friend
Karuna is my Office friend
Error happened
'''