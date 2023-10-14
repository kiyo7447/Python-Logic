import http.server
import socketserver


with socketserver.TCPServer(("127.0.0.1", 8000), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()


"""
Lean-Python> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import webbrowser
>>> webbrowser.open('http://127.0.0.1:8000')
True


# firefoxの場合
f = webbrowser.get('C:/Program Files/Mozilla Firefox/firefox.exe %s')
f.open('http://127.0.0.1:8000')

# これは失敗した。パスを通す必要がある。
f = webbrowser.get('firefox')

# Edgeの場合

f = webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s')
f.open('http://127.0.0.1:8000')

#こっちはダメだった。
f = webbrowser.get('C:/Program Files/Microsoft/Edge/Application/msedge.exe %s')

"""
