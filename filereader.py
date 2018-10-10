# f = open("/home/siddharth/Desktop/etcpasswdfile")
# for l in f.readlines():
	# print l.strip().split("/")
	# break
	# f.close()
	
import csv
with open('/home/siddharth/Desktop/etcpasswdfile', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		print (row)
		print ("\n\n")
#		print ("\n\n_______document over______\n\n")