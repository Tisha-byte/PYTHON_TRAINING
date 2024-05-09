x=int(input('enter side1:'))
y=int(input('enter side2:'))
z=int(input('enter side3:'))
if((x+y)>z and (y+z)>x and (x+z)>y):
    print("POSSIBLE")
else:
    print("NOT POSSIBLE")