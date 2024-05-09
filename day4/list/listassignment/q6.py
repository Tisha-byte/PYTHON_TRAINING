x=int(input("enter no of element in string:"))
list1=[]
for i in range(0,x):
    y = (input())
    list1.append(y)
res=list(filter(None,list1))
print(res)
