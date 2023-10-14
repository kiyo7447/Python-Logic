# -*- coding: utf-8 -*-

# Normal import
import lessen_package.util 

print(lessen_package.util.say_twice('hello'))

# AS import
import lessen_package.util as lm

print(lm.say_twice('hello'))

# From import
from lessen_package import util
# asもあんまり使わない
from lessen_package import util as ut

print(util.say_twice('hello'))

# Function import  ・・ニッチな使い方（ファンクションの所在がわからなくなる）
from lessen_package.util import say_twice

print(say_twice('hello'))

"""
__init__
lessen_package.util.say_twice:hello!
hello!hello!
lessen_package.util.say_twice:hello!
hello!hello!
lessen_package.util.say_twice:hello!
hello!hello!
lessen_package.util.say_twice:hello!
hello!hello!
"""

from lessen_package.talk import human
human.sing()
human.cry()
