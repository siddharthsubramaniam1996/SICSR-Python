import os
import datetime
print ("SIDDHARTH SUBRAMANIAM's PROGRAM TO LIST THE FILES CREATED IN THE LAST 20 minutes")
print ("---------------------------------------------------")
print ("---------------------------------------------------")

def abc():
    a = input ("input your directory path here ")

    if (a == ""):
        print ("---------------------------------------------------")
        print ("please enter a valid path for a directory")
        print ("---------------------------------------------------")
        return 0
    z=a.strip()
    b = os.listdir(z)



    print ("\n")
    print ("---------------------------------------------------")
    print ("The files created in the last 20 minutes are -")
    print ("---------------------------------------------------")
    print ("\n")

    for c in b:
        c = []
        
abc()
