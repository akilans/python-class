import argparse

def main():
    #demo_argparser()
    demo_args_kwargs()

# Argparser Demo
def demo_argparser():
    """
    Function to demo argparse
    """

    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument("-n1",default=1,help="First number",type=int)
    parser.add_argument("-n2",default=1,help="Second number",type=int)

    args = parser.parse_args()
    result = add_numbers(args.n1,args.n2)
    print(f"Addition of {args.n1} and {args.n2} is -> {result}")

def add_numbers(num1: int, num2: int) -> int:
    """
    Add two numbers
    parametes:
        num1: int
        num2: ini
    Returns:
        result: int -> num1 + num2
    """
    return num1 + num2


# Demo of *args and **kwargs
def demo_args_kwargs():
    print(square(1, 2, 3, 4, 5, 6, 7))
    # spread operator for list [ pass all elements of list as param]
    num_list = [1, 2, 3, 4]
    print(square(*num_list))

    say_details(name="Akilan", age=35, location="Tenkasi")

    akilan_details = {
        "name": "Akilan",
        "age": 35,
        "location": "Tenkasi"
    }
    # spread operator for dict [ pass all key values from dict]
    say_details(**akilan_details)

# *args is n number of arguments
def square(*args):
    square_numbers = []
    for arg in args:
        square_numbers.append(arg * arg)
    return square_numbers

# **kwargs - n number of key word arguments
def say_details(**kwargs):
    for k, v in kwargs.items():
        print(f"Key is {k} => value is {v}")


if __name__ == "__main__":
    main()

'''
Output
python 09_argparser_args_kwargs.py -n1 7 -n2 3
Addition of 7 and 3 is -> 10

[1, 4, 9, 16, 25, 36, 49]
[1, 4, 9, 16]
Key is name => value is Akilan
Key is age => value is 35
Key is location => value is Tenkasi
Key is name => value is Akilan
Key is age => value is 35
Key is location => value is Tenkasi
'''