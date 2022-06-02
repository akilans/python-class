import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir("folder1"):
    print(os.listdir())

with change_dir("folder2"):
    print(os.listdir())

with change_dir("folder3"):
    print(os.listdir())

'''
# Old way

cwd = os.getcwd()
os.chdir("folder1")
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir("folder2")
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir("folder3")
print(os.listdir())
os.chdir(cwd)

'''
