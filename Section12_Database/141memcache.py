# -*- coding: utf-8 -*-
# memcacheを使う

import sqlite3
import memcache

# memcacheに接続
db = memcache.Client(['127.0.0.1:11211'])

# memcachedへの接続状況を確認
print(f"stats: {db.get_stats()}")

# db.get_status()でmemcachedの状態を確認し、接続が無ければエラーを発生させる
if not db.get_stats():
    raise Exception('Connection failed')

# テストコード１
# memcacheに3sだけデータを保存
db.set('web_page', 'value1', time=3)
print(f"web_page: {db.get('web_page')}")

# テストコード２
# インクリメントのテスト
db.set('counter', 0, time=3)
# 1000回インクリメント
for i in range(10):
    db.incr('counter', 1)
print(f"counter: {db.get('counter')}")


# sqlite3を使う際にキャッシュサーバとして使用する
conn = sqlite3.connect('141SQLite.db')
curs = conn.cursor()
# poersonsテーブルを作成
curs.execute(
    'CREATE TABLE IF NOT EXISTS persons('
    'employ_id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'name STRING)')

# dataを削除
curs.execute('DELETE FROM persons')

# データを追加
for i in range(10):
    curs.execute(
        f'INSERT INTO persons(name) values("Mike{i}")')

# データを取得
curs.execute('SELECT * FROM persons')
print(f"personsの全件を出力する: {curs.fetchall()}")

def get_employ_id(name):
    # エラー処理がないので、そのまま使えない。
    employ_id = db.get(name)
    if employ_id:
        # memcacheにあればそれを返す
        print('get from memcache!')
        return employ_id
    # memcacheになければDBから取得
    curs.execute(f'SELECT * FROM persons WHERE name="{name}"')
    person = curs.fetchone()
    if not person:
        # DBにもなければNoneを返す
        #return None
        raise Exception('No employ')
    employ_id, name = person
    db.set(name, employ_id, time=60)    #キャッシュのタイムアウトは60s
    print('get from DB!')
    return employ_id

print(f"Mike6のemploy_id: {get_employ_id('Mike6')}")
# コミット
conn.commit()
# 接続を閉じる
conn.close()
