from neo4j import GraphDatabase

# ドライバーを初期化
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

# セッションを開始
with driver.session() as session:
    # ノードを作成
    session.run("CREATE (p:Person {name: 'John Doe', age: 30})")

    # ノードを取得
    result = session.run("MATCH (p:Person) WHERE p.name = 'John Doe' RETURN p.name AS name, p.age AS age")
    for record in result:
        print(f"{record['name']} is {record['age']} years old.")

def delete_nodes(tx):
    tx.run("MATCH (n:Person {name: 'John Doe'}) DETACH DELETE n")

# トランザクションを開始し、ノードを削除
with driver.session() as session:
    session.write_transaction(delete_nodes)

# ドライバーをクローズ
driver.close()
