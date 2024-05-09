import pandas as pd
df=pd.read_csv("Automobile_data.csv")
#print(df.head(10).dropna())  for removing rows
#print(df.head(10).dropna(axis=1))  #for droping columns
#print(df.head(10).dropna(how="any"))  #for droping
#print(df.head(10).dropna(axis=1,how="any"))  #if any value in col is null drop
#print(df.head(10).dropna(axis=1,how="all"))   #if all value is null then only drop


