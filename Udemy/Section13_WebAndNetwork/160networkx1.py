import networkx as nx
import matplotlib.pyplot as plt

# 空のグラフを作成
G = nx.Graph()

# ノードを追加
G.add_node(1)
# ボールが一つだけ表示される

nx.draw(G)
plt.show()
