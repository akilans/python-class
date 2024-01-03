'''
pip install cowsay
'''
import cowsay
import requests

def hello(name):
    cowsay.cow(f"Hello {name}")

def goodbye(name):
    print(f"Goodbye {name}")

def main():
    hello("Akilan")
    goodbye("Akilan")

if __name__ == "__main__":
    main()

