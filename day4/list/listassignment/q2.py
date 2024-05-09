x=int(input("enter no of element in string:"))
list1=[]
list2=[]
for i in range(0,x):
  y=(input())
  list1.append(y)
print(list1)
for i in range(0,x):
  z = (input())
  list2.append(z)
print(list2)
list3=[i+j for i,j in zip(list1,list2)]
print(list3)