# ユークリッド距離

import numpy as np
import matplotlib.pyplot as plt

# ユークリッド距離
def enc_dist(a, b):
    # aとbのユークリッド距離を求める
    return np.sqrt(np.sum((np.array(a)-np.array(b))**2))

# マンハッタン距離
def man_dist(a, b):
    # aとbのマンハッタン距離を求める
    return np.sum(np.abs(np.array(a)-np.array(b)))

# チェビシェフ距離
def che_dist(a, b):
    # aとbのチェビシェフ距離を求める
    return np.max(np.abs(np.array(a)-np.array(b)))

# マハラノビス距離
def mah_dist(a, b, v):
    # aとbのマハラノビス距離を求める
    return np.sqrt(np.dot(np.dot(np.array(a)-np.array(b), np.linalg.inv(v)), np.array(a)-np.array(b)))

def d(a, b):
    # aとbの距離を求める
    return enc_dist(a, b)

a=[0,0]
b=[3,1]
c=[3,4]

#
print(f"check?: {d(a,b)+d(b,c)}>{d(a,c)}")
print(f"check?: {d(b,c)+d(c,a)}>{d(b,a)}")
print(f"check?: {d(b,a)+d(a,c)}>{d(b,c)}")

# 
print(f"a-b: {d(a,b)}")
print(f"b-c: {d(b,c)}")
print(f"a-c: {d(a,c)}")

# 三角不等式を表示する
plt.plot([a[0],b[0],c[0],a[0]], [a[1],b[1],c[1],a[1]])
plt.plot([a[0],c[0]], [a[1],c[1]], linestyle='dashed')
plt.plot([b[0],c[0]], [b[1],c[1]], linestyle='dashed')
plt.plot([a[0],b[0]], [a[1],b[1]], linestyle='dashed')

# 枠を広くする
plt.xlim(-1, 4)
plt.ylim(-1, 5)

# ラベルを付ける
plt.text(-0.2, -0.2, 'a', size=20)
plt.text(3.0, 0.5, 'b', size=20)
plt.text(3.0, 4.2, 'c', size=20)
plt.show()

