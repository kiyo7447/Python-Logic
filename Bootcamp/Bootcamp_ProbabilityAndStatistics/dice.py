#
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dice = [1, 2, 3, 4, 5, 6]

x=np.random.choice(dice, size=100_000)
y=np.random.choice(dice, size=100_000)

hist,_,_=np.histogram2d(x,y,bins=len(dice),range=[[1,6],[1,6]])

# seabornのヒートマップを描く
# seabornは、xとyが逆なので注意

sns.heatmap(hist / 100_000,annot=True,xticklabels=dice, yticklabels=dice,vmax=1,vmin=0,cmap='gray_r')

sns.set(font='Meiryo')
sns.set(font_scale=1.5)
sns.set_style('whitegrid')
sns.set_palette('gray_r')
sns.set_color_codes()
sns.despine(left=True, bottom=True)
sns.set_style('whitegrid', {'grid.linestyle': '--'})
sns.set_style('whitegrid', {'grid.color': 'black'})
plt.show()
