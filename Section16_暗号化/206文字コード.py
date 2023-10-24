# Encoding: UTF-8

a = 'a'
# ord()関数は、与えられた文字のUnicodeコードポイント（整数値）を返します。
# 例: ord('a')は97を返します。
print(f"ard(a): {ord(a)}") # 97
# chr()関数は、与えられた整数値のUnicode文字を返します。
# 例: chr(97)は'a'を返します。
print(f"chr(97): {chr(97)}") # a
print(f"chr(0x61): {chr(0x61)}") # a
print(f"chr(0b1100001): {chr(0b1100001)}") # a

# hex()関数は、与えられた整数値の16進数表現を返します。
# 例: hex(255)は'0xff'を返します。
# 例: hex(97)は'0x61'を返します。
print(f"hex(97): {hex(97)}")
print(f"hex(0x61): {hex(0x61)}")
print(f"hex(0b1100001): {hex(0b1100001)}")
# bin()関数は、与えられた整数値の2進数表現を返します。
# 例: bin(10)は'0b1010'を返します。
# 例: bin(97)は'0b1100001'を返します。
print(f"bin(97): {bin(97)}")
print(f"bin(0x61): {bin(0x61)}")
print(f"bin(0b110000): {bin(0b1100001)}")
# int()関数は、与えられた値を整数に変換します。また、基数（基底）を指定することで、文字列をその基数の整数に変換することもできます。
# 例: int('10', 2)は2進数の'10'を10進数の2に変換して返します。
print(f"int('10',2): {int('10',2)}")# 2
print(f"int('10',8): {int('10',8)}")# 8
print(f"int('10',16): {int('10',16)}")# 16
print(f"int('10',32): {int('10',32)}")# 32

# complex()関数は、与えられた値から複素数を作成します。
# 例: complex(1, 2)は複素数1 + 2jを返します。
print(f"complex(1,2): {complex(1,2)}")
print(f"complex('1+2j'): {complex('1+2j')}")
print(f"complex(3,4): {complex(3,4)}")

a = 'あ'
print(f"a ord('あ'): {ord(a)}") # 12354

# Shfit-JIS
shiftjis = a.encode('shift-jis')
print(f"shiftjis    : {shiftjis}") # b'\x82\xa0'
print(f"shiftjis bin: {bin(int.from_bytes(shiftjis, 'big'))}") # 0b10000010100010
print(f"shiftjis hex: {hex(int.from_bytes(shiftjis, 'big'))}") # 0x82a0
print(f"shiftjis int: {int(int.from_bytes(shiftjis, 'big'))}") # 33440

# utf-8
# 通信で使われることが多い。
utf8 = a.encode('utf-8')
print(f"utf8    : {utf8}") # b'\xe3\x81\x82'
print(f"utf8 bin: {bin(int.from_bytes(utf8, 'big'))}") # 0b111000111000011000100010
print(f"utf8 hex: {hex(int.from_bytes(utf8, 'big'))}") # 0xe38182
print(f"utf8 int: {int(int.from_bytes(utf8, 'big'))}") # 14909826

# Unicode
# 世界中の文字を扱える。
unicode = a.encode('unicode-escape')
print(f"unicode    : {unicode}") # b'\\u3042'
print(f"unicode bin: {bin(int.from_bytes(unicode, 'big'))}") # 0b101100111000000100010
print(f"unicode hex: {hex(int.from_bytes(unicode, 'big'))}") # 0xb621
print(f"unicode int: {int(int.from_bytes(unicode, 'big'))}") # 46657


utf16 = a.encode('utf-16')
print(f"utf16: {utf16}") # b'\xff\xfeB0'
euc = a.encode('euc-jp')
print(f"euc: {euc}") # b'\xa4\xa2'
# ebcdic = a.encode('ebcdic-cp-jp') # これはエラーになる


print(f"'あ'.encode('shift-jis'): {'あ'.encode('shift-jis')}") # b'\x82\xa0'
print(f"'あ'.encode('utf-8'): {'あ'.encode('utf-8')}") # b'\xe3\x81\x82'
print(f"'あ'.encode('unicode-escape'): {'あ'.encode('unicode-escape')}") # b'\\u3042'

print(f"bytes('あ', 'shift-jis'): {bytes('あ', 'shift-jis')}") # b'\x82\xa0'
print(f"bytes('あ', 'utf-8'): {bytes('あ', 'utf-8')}") # b'\xe3\x81\x82'
print(f"bytes('あ', 'unicode-escape'): {bytes('あ', 'unicode-escape')}") # b'\\u3042'

# Base64
# 7bitのASCII文字のみで構成されるデータを、8bitのデータに変換するエンコード方式。
# 通信で使われることが多い。
import base64
print(f"base64.b64encode(b'binary'): {base64.b64encode(b'binary')}") # b'YmluYXJ5'
print(f"base64.b64decode(b'YmluYXJ5'): {base64.b64decode(b'YmluYXJ5')}") # b'binary'
print(f"base64.b64encode(b'あ'): {base64.b64encode('あ'.encode('utf-8'))}") # b'44GC'

# 画像データをBase64でエンコードする
import base64
import os

# 現在のスクリプトのディレクトリを取得する
script_dir = os.path.dirname(os.path.abspath(__file__))

# ファイルにアクセスする
with open(os.path.join(script_dir, 'frog_flying_through_the_sky.jpeg'), 'rb') as f:
    data = base64.b64encode(f.read())
    # print(f"data: {data}")

# URLエンコード
import urllib.parse
print(f"urllib.parse.quote('あ'): {urllib.parse.quote('あ')}") # %E3%81%82
print(f"urllib.parse.quote_plus('あ'): {urllib.parse.quote_plus('あ')}") # %E3%81%82
print(f"urllib.parse.unquote('%E3%81%82'): {urllib.parse.unquote('%E3%81%82')}") # あ
print(f"urllib.parse.unquote_plus('%E3%81%82'): {urllib.parse.unquote_plus('%E3%81%82')}") # あ

# urllib.parse.quoteとurllib.parse.quote_plusは、URLエンコードに使用される2つの異なる関数です。
#
# urllib.parse.quoteは、URLエンコードに使用される特殊文字をエスケープしますが、スペースを%20に置き換えません。
# 一方、urllib.parse.quote_plusは、スペースを+に置き換え、URLエンコードに使用される特殊文字をエスケープします。
#
# 例えば、文字列Hello World!をURLエンコードする場合、urllib.parse.quoteはHello%20World!を返し、
# urllib.parse.quote_plusはHello+World%21を返します。


