
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# create new list

# Method 1 - old way
my_list1 = []
for num in nums:
    my_list1.append(num * num)
print(my_list1)


# Method 2

my_list2 = [n*n for n in nums]
print(my_list2)

# Method 3
my_list3 = list(map(lambda n: n*n, nums))
print(my_list3)

# Create even num list
# Method 1
even_list1 = []
for n in nums:
    if n % 2 == 0:
        even_list1.append(n)
print(even_list1)

# Method 2
even_list2 = [n for n in nums if n % 2 == 0]
print(even_list2)


# Method 3
even_list3 = list(filter(lambda n: n % 2 == 0, nums))
print(even_list3)
