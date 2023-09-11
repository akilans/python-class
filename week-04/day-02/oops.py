""" Oops Demo"""
"""
_name - Encapsulation
class Developer(Employee) - Inheritence
details() - Abstraction
intro() - polymorphism
"""
"""Employee class"""


class Employee:

    """Init method"""

    def __init__(self, name, location, salary):
        # _name -> private property
        self._name = name
        self.location = location
        self.salary = salary

    # getter
    @property
    def name(self):
        #print("Called name getter")
        return self._name

    # setter
    @name.setter
    def name(self, name):
        #print("Called name setter")
        self._name = name

    # print(class_instance)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} -> Name - {self.name}, Location - {self.location}, Salary - {self.salary}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} -> {self.name} - {self.location} - {self.salary}"

    def details(self) -> str:
        return f"Details -> Name - {self.name}, Location - {self.location}, Salary - {self.salary}"


""" Developer class derived from Employee"""


class Developer(Employee):
    # call super init
    def __init__(self, name, location, salary, prog_lang):
        super().__init__(name, location, salary)
        self.prog_lang = prog_lang

    # not associated with class or instance(objects)
    @staticmethod
    def hello(name):
        return f"Hello, {name}"

    def say_hello(self):
        print(self.name)
        return f"Hello, I am a {self.prog_lang} Developer "


""" Manager class derived from Employee"""


class Manager(Employee):
    def __init__(self, name, location, salary, emps=None):
        super().__init__(name, location, salary)

        if emps is not None:
            self.emps = emps
        else:
            self.emps = []

    def say_hello(self):
        print(self.emps)
        return f"Hello,I am a Manager. Managing {self.emps} Employees"


def intro(obj):
    print("Printing object")
    print(obj)
    return obj.say_hello()


emp_1 = Employee("Akilan", "Tenkasi", 60000)
print(emp_1.name)
# Called name getter
# Akilan

emp_1.name = "Inba"
print("After setting name")
print(emp_1.name)
# After setting name
# Called name getter
# Inba

# details
emp_1.details()
# calls __str__ method defualt
print(emp_1)
# Employee -> Name - Akilan, Location - Tenkasi, Salary - 60000
# calls __str__ method
print(str(emp_1))


# calls __repr__ method
print(repr(emp_1))
# Employee -> Akilan - Tenkasi - 60000

dev_1 = Developer("Saurav", "Bangalore", 70000, "Rust")
# call static method
print(Developer.hello(dev_1.name))
# Hello, Saurav
mgr_1 = Manager("Madhu", "USA", 80000, [emp_1, dev_1])
print(mgr_1)
# Manager -> Name - Madhu, Location - USA, Salary - 80000


print(intro(dev_1))
print(intro(mgr_1))
