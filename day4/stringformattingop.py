#string format specifier-it is used when in string only some data is changing
#%s-string, %d-integer ,%f-float
n=input("enter name:")
a=int(input("enter age:"))
x="My name is %s and age is %d" %(n,a)
print(x)