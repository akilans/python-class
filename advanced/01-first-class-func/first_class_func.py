'''
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
'''
# calculate func execution time by adding decorator

# return func


def html_tag(tag):
    def generate_tag(text):
        return("<{0}>{1}</{0}>".format(tag, text))
    return generate_tag


h1_tag = html_tag("h1")
print(h1_tag("Hello Akilan"))

p_tag = html_tag("p")
print(p_tag("Hello Akilan"))


def square(x):
    return x * x


def cube(x):
    return x * x * x


square_func = square  # We can define func as variable
print(square_func(2))


def my_math(any_func, num_list):
    result = []
    for num in num_list:
        result.append(any_func(num))
    return result


numbers = [1, 2, 3, 4, 5]

# not caling square func, just passing as arg
square_result = my_math(square, numbers)  # paasing func as parameter
# not caling cube func, just passing as arg
cube_result = my_math(cube, numbers)


print(square_result)
print(cube_result)
