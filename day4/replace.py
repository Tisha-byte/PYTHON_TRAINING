#replace function
x="hello java nd python nd java"
print(x.replace("java","HTML"))
#replacing how many time
print(x.replace("java","HTML",1))
#split function->string to list
y=x.split(" ")
print(y)
y[5]="HTML"
print(" ".join(y))
