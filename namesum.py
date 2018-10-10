import math

string = input("Input Your Name Here : ")
print ("________________________________________________")
print ("------------------------------------------------")
string = string.lower()
d = {'a':1,
'b':2,
'c':3,
'd':4,
'e':5,
'f':6,
'g':7,
'h':8,
'i':9,
'j':10,
'k':11,
'l':12,
'm':13,
'n':14,
'o':15,
'p':16,
'q':17,
'r':18,
's':19,
't':20,
'u':21,
'v':22,
'w':23,
'x':24,
'y':25,
'z':26,
' ':0,
}
print ("the name you have entered is :",string)
print ("________________________________________________")
sum = 0
for i in string:
	sum=sum+d[i]

print ("🤗the sum of all the letters of your name is :",sum)

print ("________________________________________________")

if (sum%2==0):
	print ("number is even🎉")
	flag = 0
	print ("________________________________________________")
else:
	print ("💔number is odd😥")
	flag = 1
	print ("________________________________________________")

if (flag == 0):
	even = math.sqrt(sum)
	goodeven = math.ceil(even*100)/100
	print ("the square root of the number is",goodeven)
	print ("________________________________________________")
	print ("the square root when added to the total of the name is :",goodeven+sum)
	print ("________________________________________________")

elif (flag == 1):
	odd = sum**(1./3.)
	goododd = math.ceil(odd*100)/100
	print ("the cube root of the number is",goododd)
	result = -(goododd-sum)
	print ("________________________________________________")
	print ("the cube root when subtracted from the total of the name is :",result)	
	print ("________________________________________________")
	
	
