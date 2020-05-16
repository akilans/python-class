friends = ["Akilan","Durga","Gopi","Prashanth"]
# print(friends[0])
# print(len(friends))

'''
for number in range(11):
    print(number)
'''

for index in range(len(friends)):
    print(index)
    print(friends[index])

for friend in friends:
    print(friend)

for friend in friends:
    if friend == "Akilan":
        print("Akilan found. Dont iterate again")
        print("Performing logic for 2 mins")
        break # come out from for loop
    print(friend)
'''
print(friends[0])
print(friends[1])
print(friends[2])
'''

for friend in friends:
    if friend == "Durga":
        print("Durga found. Dont do anything")
        continue # skip this user
    print(friend)
print("Done............")