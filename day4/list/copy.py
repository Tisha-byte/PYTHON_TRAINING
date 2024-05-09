x=[12,34,56]
#copy function
y=x.copy()
y[2]="java"
print(y)
print(x)
#assignment
y=x
y[2]="java"
print(x)
print(y)
#difference between assignment and copy
#in assignment=memory address is same
#in copy function=memory address is not same