import re
str = 'abcd1234efgh5678ijkl'

m = re.findall('1+',str)
print ("the first value is")
print (m)
print (type(m))

n = re.findall('[0-9]',str)
print ("the 2nd value is")
print (n)
print (type(n))

o = re.split('\d', str)
print (o)
print (type(o))

p = re.split('\D', str)
print (p)
print (type(p))

q = re.split('^[^0-9]', str)
print (o)
print (type(q))

r = re.split('[^0-9]', str)
print (p)
print (type(r))

s = re.split('[^0-9]', str)[0].isspace()
print (s)
print (type(s))

