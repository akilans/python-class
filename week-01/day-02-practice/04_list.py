friends = ["Akilan","Duurga","Gopi"]
print(friends)
print(friends[1])
print(len(friends))

friends[1] = "Durga"

new_friend = input("Enter new friend : ")

friends.append(new_friend)
print(friends)

friends.pop(1)
print(friends)

friends = []
print(friends)