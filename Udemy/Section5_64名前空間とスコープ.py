# -*- coding: utf-8 -*-
animal = 'cat'

def f():
    """
    関数内での変数のスコープ
    """
    global animal
    print(animal)
    animal = 'dog'
    print('after', animal)
    print('locals', locals())
    print('name:', f.__name__)
    print('doc:', f.__doc__)

f()
print('global', animal)
print('globals', globals())
