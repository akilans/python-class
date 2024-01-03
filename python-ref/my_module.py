'''
pip install cowsay
'''
import cowsay

def hello(name):
    cowsay.cow(f"Hello {name}")

def goodbye(name):
    return f"Goodbye {name}"

def main():
    hello("Akilan")
    goodbye("Akilan")

if __name__ == "__main__":
    main()

