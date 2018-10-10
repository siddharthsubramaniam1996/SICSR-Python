print("The Program acts as 'Password Check' to validate password strings: \n\n")
password= input("Enter any password: ")

spe_str = '\'!@#$%^&*()[]{}"_-=.' 

if(len(password) == 12):
    for character in password:
        if(character.isupper() and character.isupper() and character not in spe_str):
           print("\nThe string entered is fit for password.")
           break
        else:
            print("\n The string entered is not fit fot password. Must contain at least one uppercase letter, one lowercase letter and one special character.\n")
            break
