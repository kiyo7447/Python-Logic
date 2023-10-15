import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]

stack1 = {
    "name": "customer1",
    "pip": ["python", "java", "go"],
    "info": {"os": "mac"},
    "data": datetime.datetime.utcnow()
}

stack2 = {
    "name": "customer2",
    "pip": ["python", "java"],
    "info": {"os": "windows"},
    "data": datetime.datetime.utcnow()
}

db_stacks = db.stacks
db_stacks.insert_one(stack2).inserted_id

stack_id = db_stacks.insert_one(stack1).inserted_id
print(f"stack_id: {stack_id}")
print(f"type stack_id: {type(stack_id)}")

from bson.objectid import ObjectId   # ObjectIdを使うためにimportする
str_stack_id = "652a8f6517d953282f4bbbe0"
# ↓文字列化したObjectIdを使う
str_stack_id = stack_id.__str__()

# print(db_stacks.find_one({{ '_id': ObjectId(f'{str_stack_id}') }})
s = db_stacks.find_one({'_id': ObjectId(str_stack_id)})
print(f"stack: {s}")

s = db_stacks.find_one({'name': 'customer2'})
print(f"stack: {s}")

# info osがwindowsのものを探す
s = db_stacks.find_one({'info.os': 'windows'})
print(f"stack: {s}")

# pipにpythonが含まれるものを探す
s = db_stacks.find({'pip': {'$in': ['python']}})


# 全てを消す
# db_stacks.delete_many({})


