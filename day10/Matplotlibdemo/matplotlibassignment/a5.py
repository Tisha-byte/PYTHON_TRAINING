from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("company_sales_data.csv")
monthlist = df ['month_number'].tolist()
m=np.arange(len(monthlist))
face_cream=df['facecream'].tolist()
face_wash=df['facewash'].tolist()
plt.bar(m-0.2,face_cream,0.4,label="Face cream sales data")
plt.bar(m+0.2,face_wash,0.4,label="Face wash sales data")
plt.title("Facewash and facecream sales data")
plt.xlabel("Month number")
plt.ylabel("Sales units in number")
plt.legend(loc="upper left")
plt.grid()
plt.show()