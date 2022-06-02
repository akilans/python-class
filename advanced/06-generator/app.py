# Generator is used to save memory

import time


def generate_emp_list(num_list):
    employees = []
    for num in num_list:
        emp = {
            "id": num,
            "name": "Akilan"
        }
        employees.append(emp)
    return employees


def generate_emp_list_gen(num_list):
    for num in num_list:
        emp = {
            "id": num,
            "name": "Akilan"
        }
        yield emp


number_list = [i for i in range(1, 10000000)]


before = time.time()
emp_list = generate_emp_list(number_list)
for emp in emp_list:
    # It actually doing some work
    continue
after = time.time()
print(f"Normal function took {after-before}")

before = time.time()
emp_list = generate_emp_list_gen(number_list)
after = time.time()
print(f"Generator function took {after-before}")
