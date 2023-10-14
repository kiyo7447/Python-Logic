# -*- coding: utf-8 -*-
import pickle

class T(object):
    def __init__(self, name) -> None:
        self.name = name

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False},
    'd': {1: 'a', 2: 'b'},
    'e': T('test')
}

with open('Section11_142pickle.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('Section11_142pickle.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(f"data_loaded: {data_loaded}")
    print(f"data_loaded['a']: {data_loaded['a']}")
    print(f"data_loaded['b']: {data_loaded['b']}")
    print(f"data_loaded['c']: {data_loaded['c']}")
    print(f"data_loaded['d']: {data_loaded['d']}")
    print(f"data_loaded['e']: {data_loaded['e']}")
