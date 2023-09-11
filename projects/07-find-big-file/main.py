import os
import json

# getting all file size of folder/subfolders


def files_size_details(target_dir):
    file_details = []
    for root_dir, _, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root_dir, file)
            file_size = f"{os.stat(file_path).st_size / 1048576:.2f}"
            file_details.append({"path": file_path, "size": float(file_size)})
    return file_details


# main function to call files_size_details function with target folder
def main():
    files_details = files_size_details("/home/akilan/Downloads")
    sorted_by_size = sorted(files_details, key=lambda i: i['size'])
    # save the result in file
    with open("file_details.json", "w") as f:
        f.write(json.dumps(sorted_by_size, indent=2))


# call the main function
if __name__ == "__main__":
    main()
