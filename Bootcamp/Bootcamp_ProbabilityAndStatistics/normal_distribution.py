# 正規分布の確率密度関数を描画する
import numpy as np
import matplotlib.pyplot as plt

all_sum=[]
# n=1000
# p=0.5

for _ in range(1000):
    sum_=0
    for _ in range(1000):
        sum_+=np.random.random()>0.5
    all_sum.append(sum_)

plt.hist(all_sum, color='aqua')
plt.show()
