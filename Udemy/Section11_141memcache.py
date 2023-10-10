﻿# -*- coding: utf-8 -*-
# memcacheを使う

import sqlite3
import memcache

# memcacheに接続
db = memcache.Client(['127.0.0.1:11211'])

# memcacheに3sだけデータを保存
db.set('web_page', 'value1', time=3)

print(f"web_page: {db.get('web_page')}")

# インクリメントのテスト
db.set('counter', 0, time=3)
# 1000回インクリメント
for i in range(1000):
    db.incr('counter', 1)

print(f"counter: {db.get('counter')}")


# sqlite3のテスト
conn = sqlite3.connect('Section11_141memcache.db')
curs = conn.cursor()
# poersonsテーブルを作成
curs.execute(
    'CREATE TABLE IF NOT EXISTS persons('
    'employ_id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'name STRING)')
# データを追加
for i in range(10):
    curs.execute(
        'INSERT INTO persons(name) values("Mike")')

# データを取得
curs.execute('SELECT * FROM persons')
print(f"persons: {curs.fetchall()}")


# コミット
conn.commit()
# 接続を閉じる
conn.close()


