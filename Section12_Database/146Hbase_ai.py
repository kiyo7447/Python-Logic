# -*- coding: utf-8 -*-
import happybase

# HBaseに接続する
connection = happybase.Connection('localhost', port=16000, autoconnect=True)
connection.open()

# テーブルを作成する
table_name = b'test_table'
column_family_name = b'cf1'
connection.create_table(table_name, {column_family_name: dict()})

r"""
kiyo@DrifterMiniPC:/mnt/c/dev/GitHub/kiyo7447/Python-Logic/Section12_Database$ python3 146Hbase_ai.py 
Traceback (most recent call last):
  File "146Hbase_ai.py", line 11, in <module>
    connection.create_table(table_name, {column_family_name: dict()})
  File "/home/kiyo/.local/lib/python3.8/site-packages/happybase/connection.py", line 303, in create_table
    if not cf_name.endswith(':'):
TypeError: endswith first arg must be bytes or a tuple of bytes, not str
"""

# データを挿入する
table = connection.table(table_name)
row_key = 'row1'
data = {'cf1:col1': 'value1', 'cf1:col2': 'value2'}
table.put(row_key, data)

# データを取得する
row = table.row(row_key)
print(row)

