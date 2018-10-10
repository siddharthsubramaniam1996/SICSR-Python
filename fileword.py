sentence=""
word=[]
f=open("filetoreadforpy.txt","r")
print('old content: \n')
print(f.read())
f.seek(0)
print('\nconverted content: \n')
for line in f:
    for splits in line.split():
        #print(splits)
        if 1==1:
            halfword = splits[1:len(splits)] + splits[:1]
            if halfword[-1:].isupper()==True:
                halfword = "Z"+ halfword
                word.append(halfword)
                halfword=" ".join(word)
                
            elif halfword[-1:].islower()==True:
                halfword = "z"+ halfword
                word.append(halfword)
                halfword = " ".join(word)
    print(halfword)
    word=[]
