import numpy as np
ar=np.arange(1,10).reshape(3,3)
x=np.sqrt(ar)   #axis=0->col,axis=1->row
print(x)
#standard deviation
x=np.std(ar)     #axis=0->col,axis=1->row
print(x)