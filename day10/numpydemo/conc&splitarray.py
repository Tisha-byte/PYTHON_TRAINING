#PYTHON NUMPY ARRY CONCTINATION AND SPLIT
import numpy as np
ar=np.arange(1,17).reshape(4,4)
ar1=np.arange(17,33).reshape(4,4)
#merging to arrays
x=np.concatenate((ar,ar1))    #by default vertically merging is done
print(x)
x=np.vstack((ar,ar1))        #vertical merging
print(x)
x=np.hstack((ar,ar1))        #horizontal merging
print(x)
#SPLIT->spliting no of parts
ar=np.arange(1,17).reshape(4,4)
x=np.split(ar,2)     #split(array_name,splitting in how many parts)
print(x)
x=np.split(ar,3)     #split(array_name,splitting in how many parts)
print(x)


