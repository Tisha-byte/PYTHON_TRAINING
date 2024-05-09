#subplot->it is used to make diffrent type of graphs from same data
import matplotlib.pyplot as plt
names=['ram','sita','sam']
marks=[89,79,90]
plt.figure(figsize=(9,3))
plt.subplot(131)     #131-> 1=row 3=size 1=column
plt.bar(names,marks)
plt.subplot(132)
plt.scatter(names,marks)
plt.subplot(133)
plt.plot(names,marks)
plt.suptitle('categorical  plotting')
plt.show()