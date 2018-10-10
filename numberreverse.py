a=123
rev=0
while(a>0):
    rev*=10
    rev=rev+(a%10)
    a=int(a/10)
print(rev)
