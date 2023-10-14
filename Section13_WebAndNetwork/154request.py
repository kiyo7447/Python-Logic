# サードパーティのライブラリrequestを使う
# pip install requests
import requests

# GETメソッドでアクセスする
payload = {"key1": "value1", "key2": "value2"}
url = "https://httpbin.org/get"
r = requests.get(url, params=payload)
print(f"status_code={r.status_code}")
print(f"text={r.text}")
print(f"response={r.json()}")

# GETメソッドでアクセスする（タイムアウトを設定する）
payload = {"key1": "value1", "key2": "value2"}
url = "https://httpbin.org/get"
# requestsモジュールのデフォルトのタイムアウトは、何も設定されていない場合にはNoneになります。つまり、リクエストが完了するまで無期限に待機します。
r = requests.get(url, params=payload, timeout=1)# 0.1だとタイム・アウトする
print(f"status_code={r.status_code}")
print(f"text={r.text}")
print(f"response={r.json()}")
# リクエストの処理時間を取得する
print(f"処理時間（elapsed）: {r.elapsed.total_seconds()}秒")

# セパレーター
print("#########################")

# POSTメソッドでアクセスする
payload = {"key1": "value1", "key2": "value2"}
url = "https://httpbin.org/post"
r = requests.post(url, data=payload)
print(f"status_code={r.status_code}")
print(f"text={r.text}")
print(f"response={r.json()}")

# セパレーター
print("#########################")

# PUTメソッドでアクセスする
payload = {"key1": "value1", "key2": "value2"}
url = "https://httpbin.org/put"
r = requests.put(url, data=payload)
print(f"status_code={r.status_code}")
print(f"text={r.text}")
print(f"response={r.json()}")

# セパレーター
print("#########################")

# DELETEメソッドでアクセスする
payload = {"key1": "value1", "key2": "value2"}
url = "https://httpbin.org/delete"
r = requests.delete(url, data=payload)
print(f"status_code={r.status_code}")
print(f"text={r.text}")
print(f"response={r.json()}")



