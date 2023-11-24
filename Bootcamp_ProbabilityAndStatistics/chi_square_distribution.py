# カイ二乗分布のグラフを描く
import numpy as np
import matplotlib.pyplot as plt

N=10_000

plt.hist(
    np.random.normal(size=N)**2
    +np.random.normal(size=N)**2
    +np.random.normal(size=N)**2
    +np.random.normal(size=N)**2, bins=100, color='aqua')

# 直接作る例
# plt.hist(np.random.chisquare(4, size=N), alpha=100, color='aqua')

plt.show()

