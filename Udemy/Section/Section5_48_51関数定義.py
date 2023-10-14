# -*- coding: utf-8 -*-
# 関数定義

# ()パレンティス

# 関数定義
def say_something():
    print("hi")

# 関数呼び出し
say_something()

# 引数を受け取る関数
def what_is_this(color):
    if color == "red":
        return "tomato"
    elif color == "green":
        return "green pepper"
    else:
        return "I don't know"

result = what_is_this("red")
print(result)

result = what_is_this("green")
print(result)

result = what_is_this("yellow")
print(result)


# 型を指定する
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
print(r)
r = add_num("a", "b")       # 型が違ってもエラーにはならない。
print(r)


# 複数の引数を受け取る関数
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

# キーワード引数
menu(entree="beef", dessert="ice", drink="beer")


