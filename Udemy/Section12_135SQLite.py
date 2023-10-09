# -*- coding: utf-8 -*-
import sqlite3

# BEGIN: 5a3f4b4f8d5c
# データベースに接続（なければ新規作成）
conn = sqlite3.connect('example.db')

try:

    # カーソルオブジェクトを作成
    c = conn.cursor()

    # テーブルを作成（既に存在する場合は何もしない）
    c.execute(
        '''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

    # データを挿入
    c.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    c.execute("INSERT INTO users (name, age) VALUES ('Bob', 40)")
    c.execute("INSERT INTO users (name, age) VALUES ('Charlie', 50)")
    c.execute("INSERT INTO users (name, age) VALUES ('Dave', 60)")
    c.execute("INSERT INTO users (name, age) VALUES ('Eve', 70)")
    c.execute("INSERT INTO users (name, age) VALUES ('Frank', 80)")
    c.execute("INSERT INTO users (name, age) VALUES ('Grace', 90)")
    c.execute("INSERT INTO users (name, age) VALUES ('Henry', 100)")
    c.execute("INSERT INTO users (name, age) VALUES ('Ivy', 110)")
    c.execute("INSERT INTO users (name, age) VALUES ('John', 120)")

    # データを読み出し
    # c.execute("SELECT * FROM users")
    # rows = c.fetchall()
    # for row in rows:
    #     print(f"id={row[0]}, name={row[1]}, age={row[2]}")

    # データが10件以上の場合は5件を残して残りを削除する
    c.execute("SELECT count(*) FROM users")
    data = c.fetchone()
    if data[0] >= 10:
        c.execute(
            "DELETE FROM users WHERE id NOT IN (SELECT id FROM users ORDER BY id DESC LIMIT 5)")

    # 変更をコミット
    conn.commit()

    # データを読み出し
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        # print(row)
        print(f"id={row[0]}, name={row[1]}, age={row[2]}")

    c.execute("SELECT count(*) FROM users")
    data = c.fetchone()
    print(f"count={data[0]}")  # 件数を表示する

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # データベース接続を閉じる
    conn.close()
# END: 5a3f4b4f8d5c
