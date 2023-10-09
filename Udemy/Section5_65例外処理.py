# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

l = [1,2,3]
i = 5

try:
    l[i]
except IndexError as ext:
    print("Don't worry: {}".format(ext))
except NameError as ex:
    print(ex)
except Exception as ex:
    # その他の例外処理 あまり良い書き方ではない。
    print("other:{}".format(ex))
else:
    # 例外が発生しなかった場合に実行される。
    print("done")
finally:
    # 例外処理の有無に関わらず、最後に実行される。
    print("clean up")

print("last")

