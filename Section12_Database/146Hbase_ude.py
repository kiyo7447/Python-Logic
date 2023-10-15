# -*- coding: utf-8 -*-
import happybase
r"""
x$ py .\146Hbase.py
Traceback (most recent call last):
  File "C:\dev\GitHub\kiyo7447\Python-Logic\Section12_Database\146Hbase.py", line 9, in <module>
    connection.create_table(b'sns', {b'blog': dict()})
  File "C:\Users\kiyot\AppData\Local\Programs\Python\Python311\Lib\site-packages\happybase\connection.py", line 303, in create_table
    if not cf_name.endswith(':'):
           ^^^^^^^^^^^^^^^^^^^^^
TypeError: endswith first arg must be bytes or a tuple of bytes, not str

Python 3.11でhappybaseライブラリを使用すると、この問題が発生する。
解決策の一つは、Pythonのバージョンをダウングレードすること。
Python 3.7や3.8など、happybaseが正常に動作することが確認されているバージョンを使用する。
"""

# HBaseに接続する
connection = happybase.Connection('localhost', port=16000)

# HBaseに接続する
connection.open()

# snsテーブルを作成する
connection.create_table(
    b'sns', 
    {
        b'blog:': dict()
    }
)

table = connection.table(b'sns')


# テーブルを作成する
table = connection.table(b'sns')

# データを追加する
table.put(b'user1', 
    {
        b'blog:bitcoin': b'user1 about bitcoin',
        b'blog:soccer': b'user1 about soccer'
    }
)

table.put(b'user2', 
    {
        b'blog:soccer': b'user2 about soccer',
        b'blog:baseball': b'user2 about baseball'
    }
)

print(f"table.scan(): {table.scan()}")
print()
print(f"table.scan(row_prefix=b'user1'): {table.scan(row_prefix=b'user1')}")
print()
print(f"table.scan(columns=[b'blog:soccer']): {table.scan(columns=[b'blog:soccer'])}")

connection.disable_table(b'sns')    
connection.delete_table(b'sns')

# HBaseから切断する
connection.close()
