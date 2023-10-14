# -*- coding: utf-8 -*-
import string

s = """\
Hi $name

$contents

Have a good day($name)
"""

t = string.Template(s)
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)
