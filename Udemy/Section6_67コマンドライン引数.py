# -*- coding: utf-8 -*-
#引数を取得する
import sys
print(sys.argv)

#引数の数を取得する
print("引数の数: " + str(len(sys.argv)))

for i in range(len(sys.argv)):
    print(f"第{i}引数: {sys.argv[i]}")

