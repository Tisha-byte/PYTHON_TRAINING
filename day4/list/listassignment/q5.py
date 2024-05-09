x=int(input("enter no of element in string:"))
list1=[]
list2=[]
for i in range(0,x):
  print("enter element for list1:")
  y=input()
  list1.append(y)
  print("enter element for list2:")
  z = input()
  list2.append(z)
print(list1)
print(list2)
k=list2.reverse()
list3=[]
list3.append(k)

for item1, item2 in zip(list1, list2):
    print(item1, item2)