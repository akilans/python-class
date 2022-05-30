import json  # just for pretty printing

employees = {
    "durga": {
        "name": "Durga",
        "age": 35,
        "height": 5.8,
        "friends": ["Akilan", "Gopal", "Siva"]
    },
    "akilan": {
        "name": "Akilan",
        "age": 33,
        "height": 5.8,
        "friends": ["Durga", "Gopal", "Siva"]
    }
}

print(employees["durga"]["age"])
employees["gopal"] = {
    "name": "Gopal",
    "age": 36,
    "height": 6.0,
    "friends": ["Durga", "Akilan", "Siva"]
}

print(employees)  # Ugly output
print(json.dumps(employees, indent=4))
