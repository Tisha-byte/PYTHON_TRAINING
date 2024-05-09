import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("company_sales_data.csv")
profitlist = df ['total_profit'].tolist()
monthlist = df ['month_number'].tolist()

#plt.plot([1,2,3],[4,5,6],'ro--')
plt.plot(monthlist,profitlist,color='red',linestyle='dashed',marker='o',markerfacecolor='black',
         linewidth=3,label="Profit data of last year")

plt.xlabel("Month Number")   #labelling x axis
plt.ylabel("Sold units number")   #labelling y axis
plt.title("Company sales data of last year")   #title
plt.legend(loc="lower right")
plt.show()
