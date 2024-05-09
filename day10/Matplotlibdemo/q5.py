import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5],[1,2,3,4,5],   'go--' ,   label = 'Delhi' , linewidth=5)
plt.plot([1,2,3,4,5],[1,4,9,16,25],   'rs-' ,   label = 'Mumbai' )
plt.axis([-2,6,0,25])
plt.legend()
plt.show()