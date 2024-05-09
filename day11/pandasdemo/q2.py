#dataframe
import pandas as pd
df=pd.DataFrame([[1,2,3,4],[5,6,7,8],[10,11,12,13]])
print(df)
dict={'id':[12,34,5],'Name':["ram","amit","rahul"]}   #dictionary passing in dataframe func
df1=pd.DataFrame(dict)
print(df1)
#*****
dict1=[{'a':12,'b':35},{'a':56,'b':90,'c':46}]    #NaN
df2=pd.DataFrame(dict1)
print(df2)
#****

