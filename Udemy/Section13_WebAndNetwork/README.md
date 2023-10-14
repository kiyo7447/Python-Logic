
# Section 13 Web and Network
## BeautifulSoap

`BeautifulSoup`で使われるパーサーには主に以下の種類があります。

1. **html.parser**: Python標準ライブラリに含まれるHTMLパーサーです。外部依存がないため、特別なインストールが不要です。しかし、速度や柔軟性では`lxml`に劣る場合があります。

2. **lxml**: 高速なXMLとHTMLのパーサーであり、`libxml2`ライブラリに基づいています。パフォーマンスが高く、また設定が豊富ですが、外部依存があります（`lxml`ライブラリをインストールする必要があります）。

3. **html5lib**: HTML5の仕様に最も忠実なパーサーですが、パフォーマンスが低いとされています。このパーサーも外部依存があります（`html5lib`ライブラリをインストールする必要があります）。

### それぞれの違い
- **速度**: `lxml` > `html.parser` > `html5lib`
- **柔軟性**: `lxml` > `html.parser` > `html5lib`
- **依存関係**: `html.parser`（なし） < `lxml`、`html5lib`（あり）

どのパーサーを使うべきかは、特定の要件や状況によります。たとえば、速度が非常に重要であれば`lxml`がお勧めですが、外部ライブラリに依存したくない場合は`html.parser`が適しています。

### 使用例
```python
from bs4 import BeautifulSoup

# html.parserを使用
soup = BeautifulSoup(html_content, 'html.parser')

# lxmlを使用
soup = BeautifulSoup(html_content, 'lxml')

# html5libを使用
soup = BeautifulSoup(html_content, 'html5lib')
```

これらの選択肢の中から、プロジェクトの要件に最も適したものを選んでください。

