""" Oops Demo"""


"""Employee class"""


class Employee:

    """Init method"""

    def __init__(self, name, location, salary):
        self.name = name
        self.location = location
        self.salary = salary

    # print(class_instance)
    def __str__(self) -> str:
        return f"{self.__class__.__name__} -> Name - {self.name}, Location - {self.location}, Salary - {self.salary}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} -> {self.name} - {self.location} - {self.salary}"


""" Developer class derived from Employee"""


class Developer(Employee):
    # call super init
    def __init__(self, name, location, salary, prog_lang):
        super().__init__(name, location, salary)
        self.prog_lang = prog_lang

    # not associated with class or instance(objects)
    @staticmethod
    def say_hello(name):
        return f"Hello, {name}"


""" Manager class derived from Employee"""


class Manager(Employee):
    def __init__(self, name, location, salary, emps=None):
        super().__init__(name, location, salary)

        if not emps:
            self.emps = emps
        else:
            self.emps = []


emp_1 = Employee("Akilan", "Tenkasi", 60000)

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
print(Developer.say_hello(dev_1.name))
# Hello, Saurav
mgr_1 = Manager("Madhu", "USA", 80000, [emp_1, dev_1])
print(mgr_1)
# Manager -> Name - Madhu, Location - USA, Salary - 80000
