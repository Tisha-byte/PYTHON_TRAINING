#tuple-immutatble,tuple cannot manupulated,update,remove
#only indexing,slicing,getting index,steping
#it is for security purpose as we cannot change it and just store it
#tuple=()
x=(12,23,45) #tuple packing
print(x)
print(type(x))

(a,b,c)=x #tuple unpacking
print(a)
#deleting tuple
del x
print(x) #written error as deleted
(a,b,c)=x
print(a)