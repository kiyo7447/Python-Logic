# -*- coding: utf-8 -*-
import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')



with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall(path='test_tar')

import shutil
shutil.rmtree('test_tar')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    """
    展開しないで中身を見る
    """
    with tr.extractfile('test_dir/test_dir2/empty.txt') as f:
        print(f.read())

"""
# tarコマンドでの解凍方法
tar zxvf test.tar.gz -C /tmp
"""
