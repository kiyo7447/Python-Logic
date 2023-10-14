# BEGIN: 7f5d9bcejpp
import pymongo

# MongoDBに接続する
client = pymongo.MongoClient("mongodb://localhost:27017/")

# データベースを作成する
db = client["mydatabase"]

# コレクションを作成する
col = db["sales"]

# Validationを設定する
validation = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["item", "quantity", "price"],
        "properties": {
            "item": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "quantity": {
                "bsonType": "int",
                "description": "must be an integer and is required",
                "minimum": 0,
                "maximum": 99_999
            },
            "price": {
                "bsonType": "decimal",
                "description": "must be a decimal and is required",
                "minimum": 0,
                "maximum": 99_999_999,
                "exclusiveMaximum": False,
                "multipleOf": 0.01
            }
        }
    }
}

# ステータスがAの売上を追加する
sales_data = {"item": "apple", "quantity": 5, "price": 0.5, "status": "A"}
col.insert_one(sales_data)

sales_data = {"item": "lemmon", "quantity": 3, "price": 1.2, "status": "A"}
col.insert_one(sales_data)

sales_data = {"item": "orange", "quantity": 2, "price": 0.8, "status": "B"}
col.insert_one(sales_data)

# ステータスがAの売上金額を集計する
result = col.aggregate([
   { "$match": { "status": "A" } },
   { "$group": { "_id": "$status", "total": { "$sum": "$price" } } }
])

# 結果を表示する
for r in result:
    print(r)
# END: 7f5d9bcejpp

