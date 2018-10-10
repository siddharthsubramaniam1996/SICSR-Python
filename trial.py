a="sid srushti srushti sid"
wordlist = a.split(' ')
print ("*********************************")
print (wordlist)
print ("---------------------------------")

wordcount = {}

cnt = 0
while cnt < len(wordlist):
	print(wordlist[cnt])
	wordcount[wordlist[cnt]] = 0
	cnt += 1

print ("---------------------------------")

cnt = 0
while cnt < len(wordlist):
	wordcount[wordlist[cnt]] +=1
	cnt +=1
print (wordcount)
print ("---------------------------------")

k = list(wordcount.keys())
cnt = 0

while cnt < len(k):
	print(k[cnt], " has occured ",wordcount[k[cnt]],"time(s)")
	cnt += 1
print ("*********************************")



