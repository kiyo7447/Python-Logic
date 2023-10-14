import networkx as nx
import matplotlib.pyplot as plt

# 空のグラフを作成
G = nx.Graph()



# ノードを追加
G.add_node(1)
G.add_node(2)
G.add_node(3)

# エッジを追加
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# グラフを描画
nx.draw(G, with_labels=True)
plt.show()
