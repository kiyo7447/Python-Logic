﻿# -*- coding: utf-8 -*-
import abc

# 抽象クラス
# 抽象クラスはあまり作らないほうがいいという話もある。
class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age
    
    # 抽象メソッド
    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError
    
    def drive(self):
        raise Exception("No drive")

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    #下記のコードをコメントアウトするとエラーになる。
    # def drive(self):
    #     print("ok")

baby = Baby()
adult = Adult()
