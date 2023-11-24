# import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib

# Meiryoフォントを使用する設定
# matplotlib.rcParams['font.family'] = 'Meiryo'

# データを読み込む
pair_list = [(15,120), (14,80), (17,150), (16,150), (16,110), (15,100), (13,70)]

# 散布図を作成する
# plt.scatter([x for x,y in pair_list], [y for x,y in pair_list])
# plt.xlabel('売上金額（万円）')
# plt.ylabel('気温（℃）')
# plt.title('売上金額と気温の散布図')
# plt.show()

x_i = [x for x,y in pair_list]
y_i = [y for x,y in pair_list]

x_bar = np.mean(x_i)
y_bar = np.mean(y_i)

numerator = np.sum([(x - x_bar) * (y-y_bar) for x,y in pair_list])
denominator1 = np.sqrt(np.sum([(x - x_bar)**2 for x,y in pair_list]))
denominator2 = np.sqrt(np.sum([(y - y_bar)**2 for x,y in pair_list]))

x_xy = numerator / (denominator1 * denominator2)
print(f'x_xy: {x_xy}') #x_xy: 0.9042001578168488


 
