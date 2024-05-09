import numpy as np
ar=np.arange(1,10).reshape(3,3)
print(ar.max())   #maximum value in array
print(ar.min())   #minimum value in array

#maximum and minimum value index
print(ar.argmax())    #maximum value's index
print(ar.argmin())     #minimum value's index

#maximum value in matrix
print(ar.max(axis=0))    #column wise
print(ar.max(axis=1))    #row wise
#minimum value in matrix
print(ar.min(axis=0))    #column wise
print(ar.min(axis=1))    #row wise
