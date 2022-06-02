import json
import requests

employees_dict = {
    1: {
        "name": "Akilan",
        "age": 35,
        "role": "Principal Software Engineer"
    },
    2: {
        "name": "Alex",
        "age": 34,
        "role": "Senior Support Engineer"
    },
}

# json.dumps convert dict to json string
emp_json_string = json.dumps(employees_dict, indent=2)
with open("emp.json", "w") as emp_file:
    emp_file.write(emp_json_string)


# json.loads json string to dict
with open("emp.json", "r") as json_file:
    emp_json_string = json_file.read()
    print(type(emp_json_string))
    emp_dict = json.loads(emp_json_string)
    print(type(emp_dict))
    print(dir(emp_dict))

print(emp_dict["1"])


res = requests.get("https://jsonplaceholder.typicode.com/posts")
print(dir(res))
print(res.status_code)
# string type
print(type(res.text))

response_dict = json.loads(res.text)

for post in response_dict:
    print(post["title"])
