import os
from os import listdir
import re

print("\n Sid's Program to change the name of the file to replace space in filenames with underscore.")
dir_path = input("Enter the name of the directory. Eg /etc/passwd/: ")

try:
    if(re.search('/[a-zA-Z]+', dir_path)):
        os.chdir(dir_path)
        os.system('ls')
        for file in listdir(dir_path):
            if ' ' in file:
                tmp = file.replace(' ', '_')
                os.rename(file,tmp)
                os.system('ls')
                
except: 
    print("the given location is not correct. please input a correct filepath")
