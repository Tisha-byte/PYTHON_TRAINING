import pandas as pd
df=pd.read_csv("Student_Result.csv")
print(df)
#group by function
g=df.groupby(by="Section")

'''for Section ,x in g:
    print(Section)
    print(x)'''
#print(g.sum())    #to find sum
print(g.agg(['sum','max','mean']))
