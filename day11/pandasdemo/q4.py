import pandas as pd
df=pd.read_csv("Automobile_data.csv")
#print(df.head(10))
print(df.head(10).isnull().sum().sum())
print(df.head(10).notnull().sum())
