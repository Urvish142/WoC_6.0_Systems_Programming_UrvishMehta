import os
import shutil
import sys

path = input("Enter path: ")

list_of_files = os.listdir(path)

for file in list_of_files:
    file_name, extension = os.path.splitext(file)

    extension = extension[1:]

    if os.path.exists(path+'\\'+extension):
        shutil.move(path+'\\'+file, path+'\\'+extension+'\\'+file)
    else:
        os.makedirs(path+'\\'+extension)
        shutil.move(path+'\\'+file, path+'\\'+extension+'\\'+file)
print("All files have been organized.")