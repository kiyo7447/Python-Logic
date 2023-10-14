import dbm

# データベースを開く
with dbm.open('140dbm.db', 'c') as db:
    # データを保存する
    db[b'key1'] = b'value1'
    db[b'key2'] = b'value2'

# データベースを開く
with dbm.open('140dbm.db', 'r') as db:
    # データを取得する
    value1 = db[b'key1']
    value2 = db[b'key2']
    print(value1, value2)

# 注意点は、stringかバイナリのみ書き込み可能
