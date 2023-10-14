import networkx as nx
import matplotlib.pyplot as plt

# 空のグラフを作成
G = nx.Graph()

# ノードを追加
G.add_node(1)
G.add_nodes_from([2,3])
G.add_edge(1, 2)
G.add_edge(2, 3)
# 1と2、2と3の間にエッジが追加される

nx.draw(G)
plt.show()
