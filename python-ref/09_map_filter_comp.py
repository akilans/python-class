def main():
    # list comprehension
    num_list = [1,2,3,4,5]
    squared_num_list = [num**2 for num in num_list]
    print(squared_num_list)

    squared_even_num_list = [num**2 for num in num_list if num % 2 == 0]
    print(squared_even_num_list)

    # Dictionary Comprehension
    friends = [
        {"name": "Alex","location":"Tenkasi"},
        {"name": "Kumar","location":"Tenkasi"},
        {"name": "Jegan","location":"Tenkasi"},
        {"name": "Kathir","location":"Coimbatore"},
        {"name": "Karuna","location":"Hyderabad"},
    ]

    tenkasi_friends = {friend["name"]: friend["location"] for friend in friends if friend["location"] == "Tenkasi"}
    print(tenkasi_friends) #{'Alex': 'Tenkasi', 'Kumar': 'Tenkasi', 'Jegan': 'Tenkasi'}

    locations = { friend["location"] for friend in friends}
    print(locations) #{'Tenkasi', 'Coimbatore', 'Hyderabad'}


    friends_dict = {"Alex":"Tenkasi","Kumar":"Tenkasi","Kathir":"Coimbatore"}
    tenkasi_friends_dict = {k:v for k,v in friends_dict.items() if v == "Tenkasi"}
    print(tenkasi_friends_dict) #{'Alex': 'Tenkasi', 'Kumar': 'Tenkasi'}


    # Map example
    squared_num_list = map(square,num_list)
    print(list(squared_num_list)) #[1, 4, 9, 16, 25]

    #Filter Example
    even_num_list = filter(is_even,num_list)
    print(list(even_num_list)) #[2, 4]

# square function
def square(num):
    return num**2

# function to check even number
def is_even(num):
    return num % 2 == 0



if __name__ == "__main__":
    main()


'''
Output:
[1, 4, 9, 16, 25]
[4, 16]
{'Alex': 'Tenkasi', 'Kumar': 'Tenkasi', 'Jegan': 'Tenkasi'}
{'Hyderabad', 'Tenkasi', 'Coimbatore'}
{'Alex': 'Tenkasi', 'Kumar': 'Tenkasi'}
[1, 4, 9, 16, 25]
[2, 4]
'''