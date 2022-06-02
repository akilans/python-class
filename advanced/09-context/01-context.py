# Own context Manager
# Context manager start with `with` keyword

class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Entered...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exit Called")
        self.file.close()


with Open_File("hello.txt", "w") as f:
    f.write("Hello Akilan \n")
    f.write("Welcome to python Context example")
