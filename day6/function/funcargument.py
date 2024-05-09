#positional argument->
def show(x,y,z):
    print(x,y,z)
show("hi","tisha","jain")
#default argument->
def show(a,b=3,c=4):   #default arguments
    print(a,b,c)
show(3)
'''def show(a=3,b,c=4):   #invalid syntax
    print(a,b,c)
show(3)'''
#keyword argument
def show(a,b,c):   #keyword arguments
    print(a,b,c)
show(c=1,a=2,b=3)
'''arbitary argument->calling can have n no of argumnt but in definition only one argument can be pass 
*=>list **=>dictionary'''
def show(*ar):
    for i in ar:
        print(i)
show(2)
show(3,4,5)
#dictionary
def show(**ar):
    for k in ar.keys() :
        print(k," :",ar[k])

show(a="java",b="hello")
show(d="python")

