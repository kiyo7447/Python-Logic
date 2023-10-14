#デスクトップアプリでじゃんけんゲームを作る
# じゃんけんゲームのルール
# 1.グー、チョキ、パーのいずれかを選択する
# 2.コンピューターもグー、チョキ、パーのいずれかを選択する
# 3.勝ち負けを判定する
# 4.勝ち負けの結果を表示する
# 5.もう一度遊ぶかどうかを選択する

import random
import tkinter as tk
from PIL import Image, ImageTk
#ログのライブラリ
import logging
#ログの出力レベルを設定
logging.basicConfig(level=logging.DEBUG)

# じゃんけんの手をリストで定義する
hand = ['グー', 'チョキ', 'パー', 'ゲーム終了']

# プログラムの開始メッセージを表示する
print('=== じゃんけんをしましょう ===')
# じゃんけんを繰り返す

logging.info("hogehoge")

