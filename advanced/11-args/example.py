# *args is n number of arguments
def square(*args):
    square_numbers = []
    for arg in args:
        square_numbers.append(arg * arg)
    return square_numbers


print(square(1, 2, 3, 4, 5, 6, 7))

# spread operator for list [ pass all elements of list as param]
num_list = [1, 2, 3, 4]
print(square(*num_list))


# **kwargs - n number of key word arguments
def say_details(**kwargs):
    for k, v in kwargs.items():
        print(f"Key is {k} => value is {v}")


say_details(name="Akilan", age=35, location="Tenkasi")

akilan_details = {
    "name": "Akilan",
    "age": 35,
    "location": "Tenkasi"
}
# spread operator for dict [ pass all key values from dict]
say_details(**akilan_details)
