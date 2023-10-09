﻿# -*- coding: utf-8 -*-
# raise IndexError('test')

class UppercaseError(Exception):
    """
    カスタム例外クラス
    """
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next') # 例外処理
