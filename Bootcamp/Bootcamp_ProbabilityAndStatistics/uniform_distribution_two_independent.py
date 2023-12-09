#
import numpy as np
import matplotlib.pyplot as plt

x=np.random.uniform(10,20,size=10000)
y=np.random.uniform(100,200,size=10000)

plt.hist2d(x,y,bins=100,range=[[0,30],[0,300]], cmap='gray_r')
plt.colorbar()

plt.show()
