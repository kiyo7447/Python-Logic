# -*- coding: utf-8 -*-

#■ 集合

"""
集合型の変数を作成する
集合型は、重複した値を持たない
集合型は、順序を持たない
集合型は、要素を追加・削除できる
集合型は、集合演算ができる
"""
s = {1,2,3,4,5,6,7,8,9,10}
print(type(s))

#からの集合を作る
s = set()
print(type(s))

#■ 複数行
st = "aaaa" \
+"bbbb"
print(st)

st = ("aaaa" 
+"bbbb")
print(st)

#■ None
n = None
# if n == None:でも可能だが、以下の方が良い
if n is None:
    print("nはNoneです")

a = 1
# if not a == 1:でも可能だが、以下の方が良い 
if a != 1:
    print("aは1ではありません")

d = {}
print(type(d))


