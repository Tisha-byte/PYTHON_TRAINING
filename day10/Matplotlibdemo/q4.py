import matplotlib.pyplot  as plt
plt.plot([1,2,3,4,5],[1,4,9,16,25],'mo--')   #'ro-'->red circle line
#plt.axis([1,5,1,25])     # [ start x axis, end x axis, start y axis, end y axis]
#plt.grid(True)
plt.xlabel("x")   #labelling x axis
plt.ylabel("y")   #labelling y axis
plt.title("STUDENT DATA")   #title
plt.show()

