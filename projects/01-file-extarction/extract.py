import os
import glob
from sys import argv
import shutil

# Get the source folder from user
src_dir = argv[1]

# List of file types and extension
files_types = {
    "docs": [".pdf", ".doc", ".txt"],
    "videos": [".mp4", ".wav"],
    "music": [".mp3"],
    "images": [".png",".jpg",".jpeg"]
}

# Create folders for each file type
for files_type in files_types:
    if not os.path.exists("organize/"+files_type):
        os.makedirs("organize/"+files_type)

# Function to filter and extract files and move to the correct folder
def move_file_by_ext(file_full_path):
    for file_type in files_types:
        for ext in files_types[file_type]:
            filename, file_extension = os.path.splitext(file_full_path)
            if file_extension == ext:
                shutil.copy(file_full_path,"organize/"+file_type+"/"+os.path.basename(filename)+file_extension)
                print("Copied successfully")

# Call the main function
for file in glob.glob(src_dir+"/*"):
    move_file_by_ext(file)