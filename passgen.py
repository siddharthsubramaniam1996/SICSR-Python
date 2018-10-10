import random

print("\nProgram to generate Random Strong Passwords\n")
passlen = int(input("Enter the length of password to generate (mandatory minimum length needs to be 12): "))

lowerChar = "abcdefghijklmnopqrstuvwxyz"
upperChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
punc = "\'!@#$%^&*()[]{}_-=.\""
charSet = lowerChar + upperChar + num + punc

passwd = [random.choice(lowerChar), random.choice(upperChar), random.choice(punc)] + [random.choice(charSet) for _ in range(passlen-3)]
random.shuffle(passwd)
print("\nthe randomly generated password is :\n")
print("".join(passwd))
print("--------------")
