#
import matplotlib.pyplot as plt
import numpy as np

def x3(x):
    return np.power(x, 3)

# -5から5まで100個のデータを生成する
x = np.linspace(-10, 10,1000)
y = x3(x)

# グラフを描画する
plt.plot(x, y, label="$x^3$")
plt.legend() # 凡例を表示する
plt.show()
