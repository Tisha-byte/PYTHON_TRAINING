import numpy as np
ar=np.arange(1,10).reshape(3,3)
x=np.sum(ar)      #sum of all the element of matrix
print(x)
x=np.sum(ar,axis=0)      #sum of all the columns of matrix
print(x)
x=np.sum(ar,axis=1)      #sum of all the row of matrix
print(x)