employees = {
    "gopi": {
        "name": "gopi",
        "age": 35,
        "friends": ["Durga","Akilan","Prashanth"],
        "address": {
            "street_name": "abc",
            "area": "feltham"
        }
    },
    "akilan": {
        "name": "akilan",
        "age": 33,
        "friends": ["Durga","Gopi","Prashanth"]
    }
}

employees["prashanth"] = {
    "name": "prashanth",
    "age": 34
}

print(employees["gopi"]["address"]["area"])

employees["gopi"]["address"]["area"] = "Slough"

print(employees["gopi"]["address"]["area"])

print(employees)