import os

#os.unlink("sample.txt")
os.mkdir("test")
for i in range(1,101):
    os.mkdir("test/folder_"+str(i))