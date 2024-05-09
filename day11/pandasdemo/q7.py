#pandas loc,iloc->for accessing grp of rows and column by label
import pandas as pd
df=pd.read_csv("Automobile_data.csv")
print(df.loc[[0,2,3,4]])
print(df.loc[0:3,"price"])    #column wise accessing

