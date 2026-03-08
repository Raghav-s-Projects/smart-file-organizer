import os
import shutil

# Folder to organize
folder_path = input("Enter folder path to organize: ")

# File type categories
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# Create folders if they don't exist
for category in file_types.keys():
    category_path = os.path.join(folder_path, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Move files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()

        for category, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(
                    folder_path, category, file))
                print(f"Moved {file} -> {category}")
                break

print("Organization complete!")
