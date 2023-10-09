# -*- coding: utf-8 -*-
# ジェネレーター
# ジェネレーターは、イテレーターを作成するための仕組み
# ジェネレーターは、関数の中でyieldを使うと作れる
# ジェネレーターは、イテレーターと同じように扱える
# ジェネレーターは、for文で繰り返し処理ができる
# ジェネレーターは、next()関数で値を取り出すことができる
# ジェネレーターは、リストなどのように一度に全ての値をメモリに展開することなく、
# 必要な時に必要な値を生成することができる
# ジェネレーターは、無限に値を生成することができる
# ジェネレーターは、無限に値を生成することができるので、
# break文でループを抜ける必要がある

l = ["Good morning", "Good afternoon", "Good night"]

for i in l:
    print(i)


def greeting():
    yield "Good morning"
    print("aaa")
    yield "Good afternoon"
    print("bbb")
    yield "Good night"  

for g in greeting():
    print(g)

g = greeting()
print(next(g))

print(next(g))

print(next(g))

# print(next(g))  # StopIterationが発生する




