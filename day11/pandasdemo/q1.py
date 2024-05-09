#pandas-> fast and efficient for data manupulation,powerful data anlysis toolkit
#function->series=>simple data,dataframe->multiple rows and columns,panel
import pandas as pd
print(pd.__version__)     #for checking version of pandas in system
se=pd.Series([12,34,56,78],index=['a','b','c','d'],dtype=float)    #for giving index of our choice
ser=pd.Series({'a':12,'b':34,'c':13})
print(se)
print(ser)
a=pd.Series([12,2,34,55,66,77])
print(a[0])    #finding value according to index value
print(a[a>2])
print(max(a))
print(min(a))

