# -*- coding: utf-8 -*-
import os

# ファイルの存在チェック
print(os.path.exists('test.txt'))
print(os.path.isfile('test.txt'))
print(os.path.isdir('design'))

#ファイルの名前を変える
# os.rename('test.txt', 'renamed.txt')

# 
if os.path.isfile('symlink.txt'):
    os.remove('symlink.txt')

os.symlink('test.txt', 'symlink.txt')

os.mkdir('test_dir')

input('enter to remove dir')

os.rmdir('test_dir')

# Ver3.5から
import pathlib
"""
"""
pathlib.Path('empty.txt').touch()

input('enter to remove file')

os.remove('empty.txt')


os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')
print(os.listdir('test_dir'))

# input('enter to remove dir')
# os.rmdir('test_dir/test_dir2')
# os.rmdir('test_dir')

p = pathlib.Path('test.csv')
print(p.read_text())

import glob
"""
glob モジュールは、Unixシェルのファイル名パターンマッチングルール（ワイルドカードなど）を使用して、
ディレクトリの内容をリスト化するために使用されます。Pythonの標準ライブラリに含まれています。
"""
pathlib.Path('test_dir/test_dir2/empty.txt').touch()

print (glob.glob('test_dir/test_dir2/*'))
import shutil
"""
Pythonの shutil モジュールは、ファイルやディレクトリの高水準の操作を行うためのユーティリティです。
shutil は "shell utilities" の短縮形で、ファイルやディレクトリのコピー、削除、移動など、
シェルコマンドで行われるような様々な操作をサポートしています。
"""
shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')

input('enter to remove file')

glob.remove('test_dir/test_dir2/*.txt')
# os.remove('test_dir/test_dir2/empty.txt')
os.rmdir('test_dir/test_dir2')
os.rmdir('test_dir')

#中身があっても削除できる
#shutil.rmtree('test_dir')

print(os.getcwd())
