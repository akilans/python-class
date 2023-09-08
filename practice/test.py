def square(x):
    return x * x


def cube(x):
    return x * x * x


print(square(2))
print(cube(2))


def my_map(any_func, numbers):
    result = []
    for number in numbers:
        result.append(any_func(number))
    return result


my_numbers = [1, 2, 3, 4, 5]

print(my_map(square, my_numbers))
print(my_map(cube, my_numbers))


def main_func(name):

    def say_hello():
        print(f"Hello {name}")

    return say_hello


hello = main_func("Inba")
hello()
