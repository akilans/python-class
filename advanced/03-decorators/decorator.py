'''
A decorator takes in a function, adds some functionality and returns it. 
'''


def div(myfunc):
    def check_for_zero(a, b):
        if b == 0:
            return "Can't be divided by zero"
        else:
            myfunc(a, b)
    return check_for_zero

# Method 2 using dec symbol


@div
def divide(x, y):
    return x / y


# Method 1 use fisrt class func
div_logic = div(divide)
print(div_logic(6, 0))

# Method 2 using decorator symbol
print(divide(5, 0))
