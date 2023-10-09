# -*- coding: utf-8 -*-
# ファイルの入出力
f = open('test.txt', 'w')
f.write('test2\n')
# こうゆう書き方もある
print('I am print', file=f)
print('My', 'name', 'is', 'Mike', sep=' ', end='!\n', file=f)
f.close()

# withを使うとcloseを書かなくてもいい
with open('test.txt', 'w') as f:
    f.write('test\n')
    print('My', 'name', 'is', 'Mike', sep=' ', end='!\n', file=f)

# ファイルの読み込み
s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'w') as f:
    f.write(s)

with open('test.txt', 'r') as f:
    print(f.read())

with open('test.txt', 'r') as f:
    """
    一行ずつ読み込む
    print(f.readline())
    """
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break


with open('test.txt', 'r') as f:
    """
    チャンクごとに読み込む
    """
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break

s = """\
123
456
789
ABC
"""
with open('test.txt', 'w') as f:
    f.write(s)
print('------------------')

with open('test.txt', 'r') as f:
    """
    ファイルのポインタを移動する
    """
    print(f.tell())
    # 0 いまの位置を教えてくれる
    print(f.read(1))
    # 1
    f.seek(5)
    print(f.read(1))
    # 4
    f.seek(14)
    print(f.read(1))
    #    -> 改行を改行を使って表示する。
    f.seek(15)
    print(f.read(1))
    # A
    f.seek(5)
    print(f.read(1))
    # 4
