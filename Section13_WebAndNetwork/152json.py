import json
j = {
    "employee": [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"}
    ]
}

# シングルクォート表示
print(f"j = {j}")

# ダブルクォート表示
# json.dumps()は、pythonのデータ型をjson形式の文字列に変換する
print(f"json j = {json.dumps(j)}")

# ファイルの書き込み
with open("152json.json", "w") as f:
    # ファイルに書き込むときは、dumpというsがないメソッドを使う
    json.dump(j, f)

# jsonファイルの読み込み
with open("152json.json", "r") as f:
    # ファイルから読み込むときは、loadというsがないメソッドを使う
    print(f"json load j = {json.load(f)}")

a = json.dumps(j)
# json.loads()は、json形式の文字列をpythonのデータ型に変換する
jo = json.loads(a)
print(f"jo = {jo}")
