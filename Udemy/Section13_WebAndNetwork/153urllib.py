"""
REST
HTTPメソッド クライアントが行いたい処理をサーバに伝える
GET データの参照
POST データの新規登録
PUT データの更新
DELETE データの削除
"""

import urllib.request
import json

# GETメソッドでアクセスする
url = "https://httpbin.org/get"
with urllib.request.urlopen(url) as f:
   res = json.loads(f.read().decode("utf-8"))
   print(f"res = {res}")
   print(f"res type = {type(res)}")

# パラメータ付きGETメソッドでアクセスする
payload = {"key1": "value1", "key2": "value2"}
url = "https://httpbin.org/get" + "?" + urllib.parse.urlencode(payload)
print(f"url = {url}")
with urllib.request.urlopen(url) as f:
   res = json.loads(f.read().decode("utf-8"))
   print(f"res = {res}")
   print(f"res type = {type(res)}")

print("#########################")

# POSTでアクセスする
payload = {"key1": "value1", "key2": "value2"}
url = "https://httpbin.org/post"
req = urllib.request.Request(
   url, data=json.dumps(payload).encode("utf-8"), method="POST")
with urllib.request.urlopen(req) as f:
    res = json.loads(f.read().decode("utf-8"))
    print(f"res = {res}")
    print(f"res type = {type(res)}")

print("#########################")

# PUTでアクセスする
payload = {"key1": "value1", "key2": "value2"}
url = "https://httpbin.org/put"
req = urllib.request.Request(
   url, data=json.dumps(payload).encode("utf-8"), method="PUT")
with urllib.request.urlopen(req) as f:
    res = json.loads(f.read().decode("utf-8"))
    print(f"res = {res}")
    print(f"res type = {type(res)}")

print("#########################")

# DELETEでアクセスする
payload = {"key1": "value1", "key2": "value2"}
url = "https://httpbin.org/delete"
req = urllib.request.Request(
   url, data=json.dumps(payload).encode("utf-8"), method="DELETE")
with urllib.request.urlopen(req) as f:
    res = json.loads(f.read().decode("utf-8"))
    print(f"res = {res}")
    print(f"res type = {type(res)}")
