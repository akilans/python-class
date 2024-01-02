def main():
    print_friends()
    print_friends_details()
    #n = get_num()
    #print_name(n)

# loop list
def print_friends():
    friends_list = ["Alex","Jegan","Kumar"]
    for friend in friends_list:
        print(friend)

# loop dict
def print_friends_details():
    friend_details = {
        "Alex": "CNR",
        "Jegan": "KLR",
        "Kumar": "PRM"
    }

    for friend in friend_details:
        print(friend,friend_details[friend],sep=" -> ")
# use while loop when there is no predefined range
def get_num():
    while True:
        n = int(input("How many times you want to say?:  "))
        if n > 0:
            break      
    return n

# for loop      
def print_name(n):
    for _ in range(n):
        print("Akilan")

# call main function
if __name__ == "__main__":
    main()