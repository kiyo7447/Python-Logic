import string
import random

from Crypto.Cipher import AES

# AES.bloc_size is 16 bytes
print(f"AES.block_size: {AES.block_size}")
print(f"string.ascii_letters: {string.ascii_letters}")
key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size))
# 16文字のランダムな文字列が生成される。
print(f"key: {key}")

# AES.block_size: 16
# string.ascii_letters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# key: vfbFFhLszyJfwlHi

iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size))
# 16文字のランダムな文字列が生成される。
print(f"iv : {iv}")

# 暗号化

# アルゴリズムは、CBCを使う。
cipher = AES.new(key.encode('shift-jis'), AES.MODE_CBC, iv.encode('shift-jis'))
# 16文字ずつ暗号化する。なので、16で割れる文字列にする。
plan_text = "Hello, World!"

padding_length =  AES.block_size - len(plan_text) % AES.block_size
# padding文字を追加する。
plan_text += chr(padding_length) * padding_length

ciper_text = cipher.encrypt(plan_text.encode('shift-jis'))
print(f"ciper_text: {ciper_text}")



# 復号化
cipher2 = AES.new(key.encode('shift-jis'), AES.MODE_CBC, iv.encode('shift-jis'))

decrypted_text = cipher2.decrypt(ciper_text)
print(f"decrypted_text: {decrypted_text}")
print(f"decrypted_text[-1]: {decrypted_text[-1]}")
print(f"decrypted_text: {decrypted_text[:-decrypted_text[-1]]}")


