a = int(input ("Enter your number to be checked here :"))	
flag = False
i = 2
j = int((a/2))+1
while (i !=j):
	if (a%i == 0):
		flag = True
		print ("Number is not prime")
		break
	i+=1
if(flag==False):
	print("no is prime")