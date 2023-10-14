# -*- coding: utf-8 -*-
# Docstrings

# 関数の説明を書く
def example_func(param1, param2):
    """Example function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    print(param1)
    print(param2)
    return True

# 関数の説明を表示する
print(example_func.__doc__)

# 関数の説明を表示する
print(help(example_func))


