import pandas as pd
df=pd.read_csv("Automobile_data.csv")
#print(df.head(10).fillna(0))
print(df.head(10).fillna(method='bfill'))  #bfile->back value fill
print(df.head(10).fillna(method='ffill'))   #ffilee->first value fill
