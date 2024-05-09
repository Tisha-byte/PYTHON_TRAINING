from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("company_sales_data.csv")
monthlist = df ['month_number'].tolist()
tooth_paste=df['toothpaste'].tolist()
x=np.array([monthlist])
y=np.array([tooth_paste])
scatter(x,y)
plt.grid(linestyle='--')
plt.xlabel("Month number")
plt.ylabel("Number of units sold")
plt.title("Tooth paste Sales data")
plt.legend(['Tooth paste sales data'])
show()