'''
Closure takes advantage of first class function
It remembers the variable defined in the inner function
'''


def greet(msg):
    greet_default_msg = "Hi,"  # It remember this message

    def printer():
        return greet_default_msg + " " + msg

    return printer


akilan_greet = greet("Akilan")
inba_greet = greet("Inba")

print(akilan_greet())
print(inba_greet())
