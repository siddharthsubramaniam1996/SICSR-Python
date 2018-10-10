print("Siddharth Subramaniam's Program to open a file, find the consecutive numbers and add them")

import re

try:
    file_path = input("Enter path to file :-  ")
    file_opened = open(file_path, "r")  # Will open the file in read mode
    file_content = file_opened.read().strip()
    file_content = re.sub('[ \t\n\r\f\v]', "", file_content)
    
    sum = 0
    
    for i in range(len(file_content)):
        if file_content[i] == file_content[i-1]:
            sum = sum + (int(file_content[i])*2)
            # Or we can also just multiply file_content[i]*2
   
   print(sum)

except FileNotFoundError:
   print("File does not exist please enter a correct path")

except ValueError:
    print("Try Again")
    print ("please enter digits exclusively in the file")
