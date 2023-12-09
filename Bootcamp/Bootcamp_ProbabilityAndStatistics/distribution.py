# 宝くじの当たる確率をシミュレーションする分布を作成する
import numpy as np
import matplotlib.pyplot as plt

# 試行回数 10000回を1000回繰り返す
# 当たる確率 0.1%

all_sum=[]
for _ in range(1000):
    for i in range(10000):
        if np.random.random()<0.001:
            all_sum.append(i)
            break

plt.hist(all_sum, bins=30, color='aqua')
plt.show()
