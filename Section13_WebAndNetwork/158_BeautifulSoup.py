from bs4 import BeautifulSoup
import requests

# HTMLを取得する
url = 'https://www.python.org'
response = requests.get(url)
html = response.content

# BeautifulSoupオブジェクトを作成する

# 
soup = BeautifulSoup(html, 'html.parser')

# タイトルタグを抽出する
title = soup.title.string

# タイトルを結果を出力する
print(f"タイトル: {title}")


# タイトルタグを抽出する
soup = BeautifulSoup(html, 'lxml')

# タイトルタグを抽出する
title = soup.find_all('title')

print(f"タイトル: {title}")



