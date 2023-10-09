# -*- coding: utf-8 -*-
# リスト内包表記

w = ["mon", "tue", "wed"]
f = ["coffee", "milk", "water"]

d = {}
for x, y in zip(w, f):
    d[x] = y
print(d)

d = {x: y for x, y in zip(w, f)}
print(d)
