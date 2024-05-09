#list3=[i+j for i,j in zip(list1,list2)]
#restriction=same of length of list1 and list2 is required
x=["m","na","i","ti"]
y=["y","me","s","sha"]

z=[i+j for i,j in zip(x,y)]
print(z)
k=[i+j for i,j in zip(x,y)]
print(k)
