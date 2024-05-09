'''MATPLOTLIB->data visulization is done using matplotlib.We can design different graphs
1)histogram, 2)bar chart, 3)scatterplots, 4)area plot, 5)pie plot, 6)error charts, 7)power spectra'''
from pylab import *
x=arange(50)*2*pi/50
#y=sin(x)
#y=cos(x)
y=tan(x)
plot(y)    #plot->it join all point by line
show()     #show is used to display graph
print(x)