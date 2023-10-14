import pymongo

# MongoDBに接続する
client = pymongo.MongoClient("mongodb://localhost:27017/")

# データベースを作成する
db = client["mydatabase"]

# コレクションを作成する
col = db["customers"]

# customersにバリデーションを設定する
# col.create_index("name", unique=True)

# addressがHから始まるデータを全て削除する
query = {"address": {"$regex": "^H"}}
x = col.delete_many(query)

# データを挿入する
data = {"name": "John", "address": "Highway 37"}
x = col.insert_one(data)

# 検索する
query = {"address": "Highway 37"}
result = col.find(query)
for r in result:
    print(r)


# データを更新する
query = {"address": "Highway 37"}
new_data = {"$set": {"address": "Park Lane 38"}}
col.update_one(query, new_data)

# データを削除する
query = {"address": "Park Lane 38"}
col.delete_one(query)

# データを挿入する
data = {"name": "John", "address": "Highway 37"}
x = col.insert_one(data)
print(f"inserted_id: {x.inserted_id}")

data = {"name": "Kiyotaka", "address": "Niigata"}
x = col.insert_one(data)
print(f"inserted_id: {x.inserted_id}")

