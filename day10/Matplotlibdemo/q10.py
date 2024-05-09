import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.DataFrame({
    'sales':[4,2,4,16,20,8],
    'signups':[7,7,8,15,17,16],
    'visits':[30,52,38,72,91,60],

}, index=pd.date_range(start='2019/01/01',end='2019/07/01',freq='M'))
ax=df.plot.area()
plt.show()
