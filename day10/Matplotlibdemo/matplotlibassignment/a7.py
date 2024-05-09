from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("company_sales_data.csv")
soap=df['bathingsoap'].tolist()
face_wash=df['facewash'].tolist()
monthlist = df ['month_number'].tolist()
plt.subplot(211,title="Sales data of bathing soap")
plt.plot(monthlist,soap,marker='o',color='black',linewidth=3)
plt.subplot(212,title="Sales data of face wash")
plt.plot(monthlist,face_wash,marker='o',color='red',linewidth=3)
plt.xlabel("Month number")
plt.ylabel("Sales units in number")
plt.show()