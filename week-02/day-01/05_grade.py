# Grade system [ 0 -100]
mark = -1

while mark < 0 or mark > 100 :
    mark = input("Enter your mark : ")
    mark = int(mark)

if mark > 0 and mark < 35:
    print("You failed")
elif mark >=35 and mark <=50:
    print("You are average")
elif mark > 50 and mark <=75:
    print("You are good")
elif mark > 75 and mark <=100:
    print("Very good")
else:
    print("You passed the exam")