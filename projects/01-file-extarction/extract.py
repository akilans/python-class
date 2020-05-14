import os
import glob
import shutil

# Get the source folder from user
src_dir = "/home/akilan/Downloads/"

# List of file types and extension
files_types = {
    "docs": [".pdf", ".doc", ".txt",".json",".csv"],
    "videos": [".mp4", ".wav"],
    "music": [".mp3"],
    "images": [".png",".jpg",".jpeg"]
}

# Create folders for each file type
for files_type in files_types:
    if not os.path.exists(src_dir+files_type):
        os.makedirs(src_dir+files_type)

# Function to filter and extract files and move to the correct folder
def move_file_by_ext(file_full_path):
    filename, file_extension = os.path.splitext(file_full_path)
    for file_type in files_types:
        if file_extension in files_types[file_type]:
            shutil.move(file_full_path,src_dir+file_type+"/"+os.path.basename(filename)+file_extension)
            break
        
# Call the main function
for file in glob.glob(src_dir+"*"):
    
    if os.path.isfile(file):
        #print(file)
        move_file_by_ext(file)
    #print("All files moved successfully")