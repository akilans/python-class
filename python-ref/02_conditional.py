# condition example
# use and | or to compare more conditional statments together
def main():
    grade()
    guess_company()

# find the number is even or not
def is_even(n):
    #return True if n %2 == 0 else False
    return n % 2 == 0

# grade function
def grade():
    score = int(input("Provide your score: "))

    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 70:
        print("Grade C")
    elif score >= 60:
        print("Grade D")
    else:
        print("Grade F")

    print(f"Is {score} is even ? - {is_even(score)}")

# function to guess friend's company
def guess_company():
    # match ( there is no switch keyword)
    friend_name = input("Provide friend name: ").lower().title()

    match friend_name:
        case "Karuna" | "Gayatri":
            print("Infosys")
        case "Hari" | "Subhasis":
            print("Oracle")
        case _:
            print("No idea")

if __name__ == "__main__":
    main()