import pandas as pd
df=pd.read_csv("Automobile_data.csv")
#df=pd.read_csv("Automobile_data.csv",nrows=1,
              # usecols=[0,3,5])     #nrows=>howw many rows you want  #usecols=for column
#df=pd.read_csv("Automobile_data.csv",index_col='company')  #for making company col as index
print(df.head())    #it gives starting five rows
print(df.tail())     #it gives last five rows


#print(df.columns)
#print(df)