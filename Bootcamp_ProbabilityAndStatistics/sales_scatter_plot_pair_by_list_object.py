import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Meiryoフォントを使用する設定
matplotlib.rcParams['font.family'] = 'Meiryo'

# データを読み込む
pair_list = [(15,120), (14,80), (17,150), (16,150), (16,110), (15,100), (13,70)]

# 散布図を作成する
plt.scatter([x for x,y in pair_list], [y for x,y in pair_list])
plt.xlabel('売上金額（万円）')
plt.ylabel('気温（℃）')
plt.title('売上金額と気温の散布図')
plt.show()
