# -*- coding: utf-8 -*-
s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'w+') as f:
    """
    w+は読み書き両方できる
    注意点は、ファイルは空になる。

    """
    f.write(s)
    f.seek(0)
    print(f.read())

try:
    with open('test2.txt', 'r+') as f:
        """
        r+は読み書き両方できる
        注意点は、ファイルが無い場合はエラーになる。    
        """
        print(f.read())
        f.write(s)
        f.seek(0)
except FileNotFoundError as ex:
    print('FileNotFoundError')
    print(ex)

