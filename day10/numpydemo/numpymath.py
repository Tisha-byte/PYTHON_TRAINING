#MATHEMATICAL OPERATION ON MATRIX USING NUMPY
import numpy as np
ar=np.arange(1,10).reshape(3,3)
ar1=np.arange(1,10).reshape(3,3)
print(ar+ar1)    #addition of two array
print(ar-ar1)      #subtraction of two array
print(ar/ar1)     #divide of two array
print(ar*ar1)      #multiplication of two array
#functions for adding different arrays
ar=np.arange(1,10).reshape(3,3)
ar1=np.arange(1,10).reshape(3,3)
#add function
x=np.add(ar,ar1)
print(x)
#subtract function
x=np.subtract(ar,ar1)
print(x)
#divide funnction
x=np.divide(ar,ar1)
print(x)
#multiply function
x=np.multiply(ar,ar1)
print(x)
#dot product
print(ar.dot(ar1))    #dot product
print(ar @ ar1)     #dot product


