x=float(input("enter the price of item:"))
y=float(input("enter GST in item %:"))
print("original cost of itrm is:")
print(x)
z=x+(y*x)/100
print("amount after adding GST:")
print(z)