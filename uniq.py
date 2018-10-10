print ("SIDDHARTH SUBRAMANIAM's Program to print unique lines \n \n")


try:
    file_path = input("Enter path to file >>> ")

    file_opened = open(file_path, "r")  # Will open the file in read mode

    file_content = file_opened.read().strip().splitlines()
    # Will read the whole file and split each line

    print("OUTPUT : Unique values in the given file :", file_path, "\n\n")

    for line in range(len(file_content)):
       
       if line == 0:
            print(file_content[line])
      
      elif file_content[line] == file_content[line-1]:
            continue
       
       else:
            print(file_content[line])

except FileNotFoundError:
    print("This file does not exist. Input the correct path")
