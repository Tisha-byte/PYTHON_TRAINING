class A:
    x=5       #public
    _x=10     #protected
    __x=50    #private
ob=A()
print(ob.x)
print(ob._x)
#print(ob.__x)      #error as it is private
print(ob._A__x)     #we can call private member using this
