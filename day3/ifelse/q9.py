phy=float(input("enter marks in physics:"))
che=float(input("enter marks in chemistry:"))
math=float(input("enter marks in maths:"))
comp=float(input("enter marks in computer:"))
bio=float(input("enter marks in biology:"))
total=phy+che+math+comp+bio
average=total/5
percentage=(total/500)*100
print("total marks:")
print(total)
print("average of marks")
print(average)
print("percentage acquired:")
print(percentage)
if(percentage>=90):
    print("A")
elif(percentage>=80):
    print("B")
elif(percentage>=70):

    print("C")
elif(percentage>=60):
    print("D")
elif(percentage>=40):
    print("E")
else:
    print("F")