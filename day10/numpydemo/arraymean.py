import numpy as np
ar=np.arange(1,10).reshape(3,3)
x=np.mean(ar)    #mean fo whole
print(x)
x=np.mean(ar,axis=0)   #column mean
print(x)
x=np.mean(ar,axis=1)   #row mean
print(x)