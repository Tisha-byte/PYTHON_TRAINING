#numpy is scientific computing library.We can perform 1D and 2D array using numpy
#1D array
import numpy as np
ar=np.array([12,34,56,78,90])  #creation of 1D array
print(ar)
print(type(ar))  #type
print(ar.ndim)    #ndim=dimention of array ie 1D,2D
#2D array
ar=np.array([[1,2,3],[4,5,6]])  #2D array creation using numpy
print(ar)
print(type(ar))  #type
print(ar.ndim) #ndim=dimention of array ie 1D,2D
print(ar.size)  #size=no of element
print(ar.shape)  #shape=row column
#ones function
ar=np.ones(5)    #ones=all value one (in float)
print(ar)
ar1=np.ones((3,3),dtype="int")  #dtype=making it int,bool
print(ar1)
#zeros function
ar=np.zeros((3,3),dtype="int")  #zeros-will give only zero
print(ar)
#arange function->creation of array
ar=np.arange(1,13)
print(ar)
ar=np.arange(1,13,3)  #3->stepping
print(ar)
#converting 1D array into 2D array
ar=np.arange(1,13).reshape(3,4)   #reshape->converting 1D into 2D
print(ar)
#linspace->dividing given range in equal ratio
ar=np.linspace(1,100,4)
print(ar)
#ravel->multidimentional to 1D array
ar=np.array([[1,2,3],[4,5,6]])
print(ar)
ar=np.array([[1,2,3],[4,5,6]]).ravel()    #2D to 1D
print(ar)
#flatten-> multidimentional to 1D
ar=np.arange(1,13).flatten()
print(ar)
#transpose->convert row to col and col to row
ar=np.arange(1,13).reshape(3,4)
print(ar)
x=ar.transpose()
print(x)




