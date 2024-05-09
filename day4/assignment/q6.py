x=input("enter a string:")
uppercount=0
lowercount=0
for i in x:
    if(i.isupper()):
        uppercount=uppercount+1
    else:
        lowercount=lowercount+1
print(uppercount)
print(lowercount)