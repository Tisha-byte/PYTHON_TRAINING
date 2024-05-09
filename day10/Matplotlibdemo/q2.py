from pylab import *
x=arange(50)*2*pi/50
y=sin(x)
#y=cos(x)
#y=tan(x)
scatter(x,y)    #scatter->it only point the points not join it
show()     #show is used to display graph
print(x)