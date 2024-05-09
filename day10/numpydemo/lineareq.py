#LINEAR EQUATIONS USING NUMPY
import numpy as np
'''8x+3y-2z=9
-4x+7y+5z=15
3x+4y-12z=35'''
A=np.array([[8,3,-2],[-4,7,5],[3,4,-12]])
b=np.array([9,15,35])
x=np.linalg.solve(A,b)
print(x)


