from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("company_sales_data.csv")
face_cream=df['facecream'].tolist()
face_wash=df['facewash'].tolist()
tooth_paste=df['toothpaste'].tolist()
m=df['moisturizer'].tolist()
soap=df['bathingsoap'].tolist()
sham=df['shampoo'].tolist()

a=round((np.sum(face_cream))/1200,2)
b=round((np.sum(m))/1200,2)
c=round((np.sum(face_wash))/1200,2)
d=round((np.sum(tooth_paste))/1200,2)
e=round((np.sum(soap))/1200,2)
f=round((np.sum(sham))/1200,2)
my_labels=["facecream","moisturizer","facewash","toothpaste","bathingsoap","shampoo"]
x=[a,b,c,d,e,f]
plt.pie(x,labels=my_labels,autopct='%.1f%%')
plt.legend(my_labels,loc="lower right")


plt.show()