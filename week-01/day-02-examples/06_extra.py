name = "Akilan"
print(len(name))
print(name.upper())
print(name.lower())
new_name = name.replace("an", "AN")
print(new_name)

# list
friends = ["Durga"]
new_friend_1 = input("Enter new friend : ")
new_friend_2 = input("Enter new friend : ")
friends.append(new_friend_1)  # Add new friend
print(friends)
friends.append(new_friend_2)  # Add new friend
print(friends)
print(len(friends))  # length of the list

# friends.remove("Durga")
print(friends)
friends.pop()
print(friends)
