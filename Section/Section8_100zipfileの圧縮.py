# -*- coding: utf-8 -*-
import zipfile
import os

# カレントディレクトリを取得して表示
current_directory = os.getcwd()
print(f"カレントディレクトリ: {current_directory}")


with zipfile.ZipFile("test.zip", "w") as z:
    """圧縮するファイルを作成する"""
    z.write("test_dir")
    z.write("test_dir/test.txt")

import  glob
with zipfile.ZipFile("test.zip", "r") as z:
    """圧縮したファイルを解凍する"""
    print(z.namelist())
    # testzzzフォルダに解凍する
    z.extractall("testzzz")
    for f in glob.glob("testzzz/**", recursive=True):
        print(f)

with zipfile.ZipFile("test.zip", "r") as z:
    with z.open("test_dir/test.txt") as f:
        print(f.read())
