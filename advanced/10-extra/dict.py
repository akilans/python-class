num_list = [1, 2, 3, 4]
letter_list = ["A", "B", "C", "D"]

my_dict1 = {}
for num in num_list:
    for letter in letter_list:
        my_dict1[letter] = num
        letter_list.remove(letter)
        break
print(my_dict1)
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}

num_list = [1, 2, 3, 4]
letter_list = ["A", "B", "C", "D"]
my_dict2 = {l: n for n in num_list for l in letter_list}
print(my_dict2)
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}

num_list = [1, 2, 3, 4]
letter_list = ["A", "B", "C", "D"]
print(dict(zip(letter_list, num_list)))
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}
