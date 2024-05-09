import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("company_sales_data.csv")
profitlist = df ['total_profit'].tolist()
monthlist = df ['month_number'].tolist()
plt.plot(monthlist,profitlist,label='Month-wise profit data of last year',color='m')
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.xticks(monthlist)
plt.title('company profit per month')
plt.yticks([100000,200000,300000,400000,500000])
plt.show()