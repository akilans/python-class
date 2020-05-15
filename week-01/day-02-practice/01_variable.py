# data types 

# string, int, float, array [ list, tuples, dictionary ]
'''
Here is
my multiline
command
'''
name = "gopi"
age = 35 # integer
height = 5.8 # float
friends = ["Durga","Akilan","Prashanth"]
coordinates = (2,5)

print(type(name))
print(type(age))
print(type(height))
print(type(coordinates))

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

print(type(employees))