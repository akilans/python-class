import os

folder_name = "durga"

if os.path.exists(folder_name):
    print("Folder already exits")
else:
    os.mkdir(folder_name)

folder_path = "./"
desktop_data = os.listdir(folder_path)
number_of_folder = 0
number_of_files = 0

for file_item in desktop_data:
    if os.path.isfile(folder_path+file_item):
        number_of_files = number_of_files + 1
    else:
        number_of_folder = number_of_folder + 1

print("Number of folders - " + str(number_of_folder))
print("Number of files - " + str(number_of_files))

# os.remove("test.csv")
