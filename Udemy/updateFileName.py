import os

folder_path = "."

for filename in os.listdir(folder_path):
    prefix = "Section11_"
    if prefix in filename:
        new_filename = filename.replace(prefix, "")
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
