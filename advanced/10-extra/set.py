duplicate_list = [1, 8, 9, 3, 2, 5, 1, 3, 2, 7, 7, 4, 3, 9, 7, 8]
my_set1 = set()

# Method 1
for num in duplicate_list:
    my_set1.add(num)

print(my_set1)

# Method 2
my_set2 = {n for n in duplicate_list}
print(my_set2)
