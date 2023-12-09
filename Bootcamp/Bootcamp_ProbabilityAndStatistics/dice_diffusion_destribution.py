#
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dice = [1, 2, 3, 4, 5, 6]

x=np.random.choice(dice, size=100_000)
y=[]

for trial_x in x:
    trial_y=sum([np.random.choice([0,1]) for _ in range(trial_x)])
    y.append(trial_y)

hist,_,_=np.histogram2d(x,y,bins=(len(dice),len(dice)+1),range=[[1,6],[0,6]])

# seabornは、xとyが逆なので注意

sns.heatmap(hist / 100_000,annot=True,xticklabels=[0]+dice, yticklabels=dice)

sns.set(font='Meiryo')
sns.set(font_scale=1.5)
sns.set_style('whitegrid')
sns.set_palette('gray_r')
sns.set_color_codes()
sns.despine(left=True, bottom=True)
sns.set_style('whitegrid', {'grid.linestyle': '--'})
sns.set_style('whitegrid', {'grid.color': 'black'})

plt.xlabel('サイコロの出目')
plt.ylabel('表の出る回数')
plt.title('サイコロを振った回数と表の出る回数の関係')
#日本語を表示できるようにする
plt.rcParams["font.size"] = 14
plt.rcParams['font.sans-serif'] = ['Meiryo']
plt.show()
