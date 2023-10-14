# -*- coding: utf-8 -*-
# ラムダ
l= {"Mon", "tue", "Wed", "Thu", "fri", "sat", "Sun"}

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)

# ラムダを使うと、以下のように書くこともできる。
sample_func2 = lambda word: word.capitalize()
change_words(l, sample_func2)

# 1行で書く場合は、以下のように書くこともできる。
change_words(l, lambda word: word.capitalize())
