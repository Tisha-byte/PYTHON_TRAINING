import matplotlib.pyplot as plt
from pandas import read_csv
filename = 'indians-diabetes.csv'
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data=read_csv(filename,names=names)
#data.hist()
#data.plot()

plt.show()