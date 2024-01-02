def main():
    x = get_int()
    print(f"Value of x is {x}")

# get int
# use try and except to handle error
def get_int():
    while True:
        try:
            x = int(input("Enter a valid number: "))
        except ValueError:
            print("It is not a integer")
        #except Exception as e:
        #    print(e)
        else:
            return x

# call main function
if __name__ == "__main__":
    main()