import numpy as np

# 外れ値なし
print("外れ値なし")
x = [3,4,5,3,4,5,3,4,5]
print("平均値：", np.mean(x))
print("中央値：", np.median(x))
print("最頻値：", np.bincount(x).argmax())
print("標準偏差：", np.std(x))
print("分散：", np.var(x))

# 外れ値あり
print("外れ値あり")
x = [3,4,5,3,4,5,3,4,5,100]
print("平均値：", np.mean(x))
print("中央値：", np.median(x))
print("最頻値：", np.bincount(x).argmax())
print("標準偏差：", np.std(x))
print("分散：", np.var(x))

# Path: Bootcamp/mean_median_mp.py
"""
外れ値なし
平均値： 4.0
中央値： 4.0
最頻値： 3
標準偏差： 0.816496580927726
分散： 0.6666666666666666

外れ値あり
平均値： 13.6
中央値： 4.0
最頻値： 3
標準偏差： 28.810414783546594
分散： 830.0400000000002
"""

