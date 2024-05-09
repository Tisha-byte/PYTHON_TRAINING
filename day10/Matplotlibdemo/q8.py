import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)
dt=0.01
t = np.arange(0,10,dt)
nse=np.random.randn(len(t))
r=np.exp(-t/0.05)
cnse=np.convolve(nse,r)* dt
cnse= cnse[:len(t)]
#defaultt
s = 0.01 * np.sin(2 * np.pi * t) + cnse
print(s)
plt.subplot(211)
plt.title('Example 1:Default')
plt.plot(t,s)
plt.subplot(212)
plt.psd(s,512,1 /dt)
plt.show()
