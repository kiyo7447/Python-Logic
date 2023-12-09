# ２変数の非独立な正規分布（例：気温と売上金額）からなるデータを作成し、ヒストグラムを描く
import numpy as np
import matplotlib.pyplot as plt

x=np.random.normal(15,3,size=100_000)
e=np.random.normal(0,30,size=100_000)
y=10*x+e

plt.hist2d(x,y,bins=100,range=[[0,30],[0,300]], cmap='gray_r')
plt.colorbar()

plt.show()
