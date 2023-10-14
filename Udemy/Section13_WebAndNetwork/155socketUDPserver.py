"""
ウェルノウンポート番号 0-1023
登録済みポート番号 1024-49151
動的・プライベートポート番号 49152-65535
"""

# ソケットオブジェクトの作成
# AF_INET:IPv4
# SOCK_STREAM:TCP
# SOCK_DGRAM:UDP

# TCPIPを使う
# import socket
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     # サーバーを指定
#     s.bind(("127.0.0.1", 50007))
#     s.listen(1) # 接続の待ち受け（キューの最大数を指定）
#     while True:
#         conn, addr = s.accept() # 接続の受付
#         while True:
#             data  = conn.recv(1024)
#             if not data:
#                 break
#             print(f"data: {data}, addr: {addr}")
#             conn.sendall(b"Received: " + data)

# UDPを使う
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(("127.0.0.1", 50007))
    while True:
        data, addr = s.recvfrom(1024)
        print(f"data: {data}, addr: {addr}")
        s.sendto(b"Received: " + data + b" add Server Message", addr) # クライアントにデータを返す
