# main function
def main():
    hello()
    name = input("What's your name? ").strip().upper()
    hello(name)
    x = int(input("Enter x: "))
    print(f"Square value of {x} is {square(x)}")

# function with return value
def square(n):
    return n * n

# function without return value
def hello(to="World"):
    print("Hello,",to)
    print(f"Hello, {to}")
    print("DevOps","Docker","Kubernetes","AWS","Python",sep="|",end="\n")

# it will get executed only when call the script directly
# if we import into other script it will not get executed
# python 01_func_variable.py
if __name__ == "__main__":
    main()


'''
Output:
Hello, World
Hello, World
DevOps|Docker|Kubernetes|AWS|Python
What's your name? Akilan
Hello, AKILAN
Hello, AKILAN
DevOps|Docker|Kubernetes|AWS|Python
Enter x: 5
Square value of 5 is 25
'''