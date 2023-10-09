# -*- coding: utf-8 -*-

class Person(object):
    kind = "human"

    def __init__(self):
        self.x = 100

    def what_is_your_kind(self):
        return self.kind

    # クラスメソッド
    @classmethod
    def what_is_your_kind2(self):
        return self.kind

    @staticmethod
    def about(year):
        print(f"about human:{year}") 

a = Person()
print(a)
# <__main__.Person object at 0x00000231FCF7A950>
# インスタンス化されたオブジェクトが表示される。

print(a.x)
# 100

print(a.what_is_your_kind())
# human

print(a.kind)
# human

a.about(2003)
# about human:2003

b = Person
print(b)
# <class '__main__.Person'>
# クラスのままです。

# print(b.x)
# AttributeError: type object 'Person' has no attribute 'x'
# クラス変数はインスタンス化されたオブジェクトには存在しない。

# クラスメソッドを呼ぶ
print(b.what_is_your_kind2())

Person.about(1999)
# about human:1999
