def say_hello():
    return "Hello"

def say_hello_with_name(name="Durga"):
    return "Hello "+ name

def get_full_name(fname,lname):
    full_name = fname +" "+ lname
    length_of_name = len(full_name)
    return full_name, length_of_name