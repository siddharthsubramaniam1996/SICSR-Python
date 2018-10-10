print("Siddharth Subramaniam's Program to find users in /etc/passwd and display them")


try:
    file_path = '/etc/passwd'
    file_opened = open(file_path, "r")  # Will open the file in read mode
    file_content = file_opened.read().strip().splitlines()
    # Will read the whole file and split each line
    
    for line in file_content:
        content = line.split(':')
        print(content[0])

except FileNotFoundError:
    print("File does not exist please enter a correct path")
