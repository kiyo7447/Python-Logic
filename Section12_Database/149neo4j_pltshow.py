from neo4j import GraphDatabase
import matplotlib.pyplot as plt

# Neo4jへの接続情報
uri = "bolt://localhost:7687"
user = "neo4j"
password = "password"

# Neo4jへのクエリ
query = "MATCH (n) RETURN id(n), n.name"

# Neo4jへの接続
driver = GraphDatabase.driver(uri, auth=(user, password))
with driver.session() as session:
    result = session.run(query)

    # データの取得
    nodes = []
    labels = []
    for record in result:
        nodes.append(record[0])
        labels.append(record[1])

# グラフのプロット
plt.figure(figsize=(10, 10))
plt.scatter(nodes, nodes, s=1000, alpha=0.5)
for i, label in enumerate(labels):
    plt.annotate(label, (nodes[i], nodes[i]), fontsize=12)
plt.show()
