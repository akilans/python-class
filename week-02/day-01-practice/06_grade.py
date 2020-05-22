mark = -1

# Get the correct value from user
while mark < 0 or mark > 100:
    mark = input("Enter mark b/w 0-100 : ")
    mark = int(mark)

#Logic here
print(mark)

#>0 and <35  Fail
if mark < 35:
    print("You failed the exam!")
# > 35 and <=50 - average
elif mark >= 35 and mark <= 50:
    print("You are average")
elif mark >50 and mark <= 75:
    print("Good....")
elif mark >75 and mark <= 100:
    print("Very Good")
else:
    print("Wrong with logic")