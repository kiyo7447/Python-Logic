import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Meiryoフォントを使用する設定
matplotlib.rcParams['font.family'] = 'Meiryo'

# データを読み込む
data = pd.read_csv('data.csv')

# 散布図を作成する
plt.scatter(data['売上金額'], data['気温'])
plt.xlabel('売上金額（万円）')
plt.ylabel('気温（℃）')
plt.title('売上金額と気温の散布図')
plt.show()
