x=int(input("enter a number of element in list:"))
list1=[]
list2=[]
for i in range(0,x):
  y=int(input())
  list1.append(y)
for i in list1:
    z=i*i
    list2.append(z)
print(list2)