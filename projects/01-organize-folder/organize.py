import os
import glob
import shutil

# Get the source folder from user [Change as per your folder structure]
src_dir = "/home/akilan/Downloads/"

# List of file types and extension
files_types = {
    "docs": [".pdf", ".doc", ".txt",".json",".csv"],
    "videos": [".mp4", ".wav"],
    "music": [".mp3"],
    "images": [".png",".jpg",".jpeg"]
}

# Get the folder name by file extension
def get_folder_name_by_ext(ext):
    for file_type in files_types:
        if ext in files_types[file_type]:
            return file_type # return the folder
    
    return "others" # If not found return "others" folder

# Call the main function
for file in glob.glob(src_dir+"*"):
    
    if os.path.isfile(file):
        filename, file_extension = os.path.splitext(file)
        folder_name = get_folder_name_by_ext(file_extension)
        # Create folder if not exists
        if not os.path.exists(src_dir+folder_name):
            os.makedirs(src_dir+folder_name)
        # ove file
        shutil.move(file,src_dir+folder_name+"/"+os.path.basename(filename)+file_extension)
    else:
        print("Skipping folder - "+ file)