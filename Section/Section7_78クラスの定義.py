# -*- coding: utf-8 -*-
s = 'パタトクカシーー'
#パトカー
print(s[::2])
# タクシー
print(s[1::2])
print(s.capitalize())

class Person(object):
    """
    人を表すクラス
    クラス変数ageは全インスタンスで共有する
    """
    kind = 'human'
    def __init__(self, name):
        """
        コンストラクタ
        """
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        print('I am {}'.format(self.kind))
        self.run(10)

    def run(self, num):
        print('run' * num)

    def __del__(self):
        """
        デストラクタ
        """
        print('good bye')

# クラスの使い方
person = Person('Mike')
person.say_something()
del person
