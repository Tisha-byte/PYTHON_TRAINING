'''variable-local variable=>cannot access anywhere can access in only its function,
global variable=>can be access anywhere'''
x=5 #global variable
def show():
    y=10  #local variable
    print(x)
def put():
    z=30  #local variable
    print(x)
show()
put()
'''if we want to redefine global variable in func we have to intialize it with global keyword 
in function definition'''

