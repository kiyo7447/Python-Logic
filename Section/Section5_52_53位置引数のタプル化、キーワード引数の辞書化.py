# -*- coding: utf-8 -*-



# 位置引数のタプル化
def say_something(word, *args):
    print("word = ", word)
    for arg in args:
        print(arg)

say_something("Hi!", "Mike", "Nance")
# 出力結果
""""
word =  Hi!
Mike
Nance
"""


# キーワード引数の辞書化
def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu("banana", "apple", "orange", entree="beef", drink="coffee")

# 出力結果
"""
banana
('apple', 'orange')
{'entree': 'beef', 'drink': 'coffee'}

"""