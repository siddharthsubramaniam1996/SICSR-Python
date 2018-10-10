

print("Siddharth's Program for Transforming Words \n")
print("Enter file path: ",end=" ")
filepath = input()

file = open(filepath)
data = file.read()
file.close()

print("\n---File Content---")
print(data,end="\n\n")

print("--After Transforming--")
for line in data.split("\n"):
	rline = []
	for word in line.split():
		word = word + word[0]
		if word[0].isupper():
			word = word.replace(word[0],"Z",1)
		else:
			word = word.replace(word[0],"z",1)
		rline.append(word)
	print(" ".join(rline))
	
print ("\n\n------program over------\n\n")
