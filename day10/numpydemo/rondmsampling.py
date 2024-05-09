import numpy as np
import random
ar=np.random.random((3,3))
print(ar)
#for integer value
ar=np.random.randint(1,4,(4,4))     #randint->for integer
print(ar)
#random value ko fix krne k liy func h->seed
np.random.seed(10)     #seed->fix any random value
ar=np.random.randint(1,4,(4,4))     #randint->for integer
print(ar)

