#ARRAY SLICING
import numpy as np
ar=np.arange(1,101).reshape(10,10)
#[ , ]  before comma->row,after comma->column
print(ar[0,0])    #[row,column]
print(ar[0])      #0th row
print(ar[2])      #2nd  row
print(ar[ : ,0])   #1st column
print(ar[ : 2, :2])     #[start row : last row : stepping,column start : column end : stepping]


