employees = {}

name = input("Enter Name : ")
age = input("Enter Age : ")
friends = ["Akilan","Durga", "Gopal"]

employees[name] = {
    "emp_name": name,
    "emp_age": age,
    "emp_frinds": friends
}

print(employees)