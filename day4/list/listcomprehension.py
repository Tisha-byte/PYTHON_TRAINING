#list comprehension=performing any process in list in just one line
x=[1,2,3,4]
y=[i*2 for i in x]
print(y)
p=[i for i in range(20) if i%2==0]
print(p)
o=[i for i in range(30) if i%2!=0]
print(o)