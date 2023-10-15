from neo4j import GraphDatabase
import matplotlib.pyplot as plt

# ドライバーを初期化
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

# データをすべて消す
def delete_all(tx):
    tx.run("MATCH (n) DETACH DELETE n")

# トランザクションを開始し、ノードを削除
with driver.session() as session:
    session.execute_write(delete_all)


# ノードを作成
def create_nodes(tx, nodes):
    query = """
    UNWIND $nodes AS node
    CREATE (:Person {name: node.name, age: node.age});
    """
    tx.run(query, nodes=nodes)

# ノードデータのリスト
nodes_data = [{"name": "Billy Kane", "age": 30},
              {"name": "Raiden", "age": 30}, 
              {"name": "Geese Howard", "age": 30}]


# トランザクションを開始し、ノードを作成
with driver.session() as session:
    session.execute_write(create_nodes, nodes_data)

# 関係を作成
def create_relationships(tx, relationships):
    query = """
    UNWIND $relationships AS rel
    MATCH (a:Person {name: rel.person1}), (b:Person {name: rel.person2})
    CREATE (a)-[:RELATION {type: rel.type}]->(b);
    """
    tx.run(query, relationships=relationships)
# ここでリレーション名を動的に変更することはとても難易度が高い。

# 関係データのリスト
relationships_data = [
    {"person1": "Geese Howard", "person2": "Raiden", "type": "UNDERLING"},
    {"person1": "Geese Howard", "person2": "Billy Kane", "type": "UNDERLING"},
    {"person1": "Raiden", "person2": "Billy Kane", "type": "KNOWS"},
    {"person1": "Billy Kane", "person2": "Raiden", "type": "KNOWS"}
]

# トランザクションを開始し、関係を作成
with driver.session() as session:
    session.execute_write(create_relationships, relationships_data)

# セッションを開始
# with driver.session() as session:
#     # ノードを作成
#     r"""
#     CREATE (:Person {name: 'Tung Fu Rue'}),
#         (:Person {name: 'Duck King'}),
#         (:Person {name: 'Richard Myer'});
#     """
#     session.run("CREATE (p:Person {name: 'Billy Kane', age: 30}),"
#     "(p:Person {name: 'Raiden', age: 30}),"
#     "(p:Person {name: 'Geese Howard', age: 30});")

#     # 関係を作成
#     r"""
#     MATCH (tung:Person {name: 'Tung Fu Rue'}), (duck:Person {name: 'Duck King'}), (bill:Person {name: 'Richard Myer'})
#     CREATE (tung)-[:KNOWS]->(duck),
#         (tung)-[:KNOWS]->(bill),
#         (duck)-[:KNOWS]->(bill);
#     """
#     session.run("MATCH (geese:Person {name: 'Geese Howard'}),"
#                 "(raiden:Person {name: 'Raiden'}),"
#                 "(billy:Person {name: 'Billy Kane'})"
#                 "CREATE (geese)-[:UNDERLING]->(raiden),"
#                 "(geese)-[:UNDERLING]->(billy),"
#                 "(raiden)-[:KNOWS]->(billy) RETURN type(r)"
#                 "(billy)-[:KNOWS]->(raiden) RETURN type(r)")




def get_data(tx):
    # データの準備
    nodes = set()
    edges = []

    # データを取得
    result = tx.run("MATCH (a)-[r]->(b) RETURN a.name, type(r), b.name LIMIT 25")
    for record in result:
        nodes.add(record[0])
        nodes.add(record[2])
        edges.append((record[0], record[2]))
    return nodes, edges

with driver.session() as session:
    nodes, edges = session.execute_read(get_data)

# ノードの座標を準備（ここでは簡単のためにランダムな座標を使用）
# import random
# node_coords = {node: (random.random(), random.random()) for node in nodes}
node_coords = {node: (i, i) for i, node in enumerate(nodes)}

# グラフのプロットをいい感じにする
# ノードとリレーションの位置を合わせる
for edge in edges:
    x_coords = [node_coords[edge[0]][0], node_coords[edge[1]][0]]
    y_coords = [node_coords[edge[0]][1], node_coords[edge[1]][1]]
    # リレーションシップの中点を求める
    mid_x = sum(x_coords) / 2
    mid_y = sum(y_coords) / 2
    # ノードの座標をリレーションシップの中点にする
    node_coords[edge[0]] = (mid_x, mid_y)
    node_coords[edge[1]] = (mid_x, mid_y)

plt.figure(figsize=(10, 10))
# nodesの円を3000の大きさで描画、背景色はピンクにする。
plt.scatter(list(nodes), list(nodes), s=3000, alpha=0.5, c='pink')
for edge in edges:
    x_coords = [node_coords[edge[0]][0], node_coords[edge[1]][0]]
    y_coords = [node_coords[edge[0]][1], node_coords[edge[1]][1]]
    plt.plot(x_coords, y_coords, 'k-')  # リレーションシップを描画
for node, coords in node_coords.items():
    plt.text(coords[0], coords[1], node)  # ノード名を描画

# 軸ラベルとタイトルを設定する
plt.xlabel('Node')
plt.ylabel('Node')
plt.title('Fatal Fury Node Graph')

# フォントサイズを調整する
plt.tick_params(labelsize=12)

# グリッドを表示する
plt.grid()

# 
plt.show()


# with driver.session() as session:
#     # ノードを取得
#     # result = session.run("MATCH (p:Person) WHERE p.name = 'John Doe' RETURN p.name AS name, p.age AS age")
#     # result = session.run("MATCH (n:Person) RETURN n LIMIT 25")
#     result = session.run("MATCH (n) RETURN id(n),n.name, n.age")

#     # データの取得
#     nodes = []
#     labels = []
#     for record in result:
#         nodes.append(record[0])
#         labels.append(record[1])

# # グラフのプロット
# plt.figure(figsize=(10, 10))
# plt.scatter(nodes, nodes, s=1000, alpha=0.5)
# for i, label in enumerate(labels):
#     plt.annotate(label, (nodes[i], nodes[i]), fontsize=12)
# # nodesを使って、関係をプロットする。
# for i, node in enumerate(nodes):
#     plt.annotate(node, (nodes[i], nodes[i]), fontsize=12)
# plt.show()

# ドライバーをクローズ
driver.close()
