# -*- coding: utf-8 -*-
import happybase
r"""
https://happybase.readthedocs.io/en/latest/
"""
connection = happybase.Connection('127.0.0.1', port=16000)


# create table
connection.create_table(
    'table-name',
    {'cf1': dict(max_versions=10),
     'cf2': dict(max_versions=1, block_cache_enabled=False),
     'cf3': dict(),  # use defaults
    }
)
r"""
  File "C:\Users\kiyot\AppData\Local\Programs\Python\Python311\Lib\site-packages\thriftpy2\transport\socket.py", line 131, in read
    raise TTransportException(type=TTransportException.END_OF_FILE,
thriftpy2.transport.base.TTransportException: TTransportException(type=4, message='TSocket read 0 bytes')
"""

table = connection.table('table-name')

table.put(b'row-key', {b'family:qual1': b'value1',
                       b'family:qual2': b'value2'})

row = table.row(b'row-key')
print(row[b'family:qual1'])  # prints 'value1'

for key, data in table.rows([b'row-key-1', b'row-key-2']):
    print(key, data)  # prints row key and data for each row

for key, data in table.scan(row_prefix=b'row'):
    print(key, data)  # prints 'value1' and 'value2'

row = table.delete(b'row-key')
