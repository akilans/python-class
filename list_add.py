friends = []
friend_1 = input("Enter your 1st friend 1 : ")
friend_2 = input("Enter your 1st friend 2 : ")
friend_3 = input("Enter your 1st friend 3 : ")

friends.append(friend_1)
friends.append(friend_2)
friends.append(friend_3)

print(friends)
print("Number of friends "+ str(len(friends)))

print("Your best frineds are - "+ str(friends))