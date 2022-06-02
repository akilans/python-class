from contextlib import contextmanager


@contextmanager
def Open_File(filename, mode):
    '''
    f = open(filename, mode)
    yield f
    f.close()
    '''
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()


with Open_File("hello.txt", "w") as f:
    f.write("Hello Akilan \n")
    f.write("Context manager with context manager decorator")


print(f.closed)
