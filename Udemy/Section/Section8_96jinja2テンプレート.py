# -*- coding: utf-8 -*-
# pip install jinja2

from jinja2 import Template, Environment
from datetime import datetime
from memory_profiler import profile

@profile
def print_html() :
    s = """\
    <!DOCTYPE html>
    <html>
        <body>
            <h1>My Items</h1>
            <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
            </ul>
        </body>
    </html>
    """

    t = Template(s).render(items=['banana', 'mango', 'apple'])
    print(t)

# これを実行すると、以下のようなHTMLが出力される。
"""
<!DOCTYPE html>
<html>
    <body>
        <h1>My Items</h1>
        <ul>

            <li>banana</li>

            <li>mango</li>

            <li>apple</li>

        </ul>
    </body>
</html>
"""

"""
from jinja2 import Environment, FileSystemLoader

# テンプレートが存在するディレクトリを指定
env = Environment(loader=FileSystemLoader('path/to/templates/directory'))

# テンプレートを読み込む
template = env.get_template('template.html')

# データを指定
data = {
    'items': ['Item 1', 'Item 2', 'Item 3']
}

# データをテンプレートに適用
output = template.render(data)

print(output)

"""

# ljust custom filter

def ljust_filter(s, width=10):
    return str(s).ljust(width)

def rjust_filter(s, width=10):
    return str(s).rjust(width)

# 日付フォーマットのカスタムフィルターを追加
def date_format_filter(date_str, format='%Y年%m月%d日', informat='%Y-%m-%d' ):
    return datetime.strptime(date_str, informat).strftime(format)

# number_format custom filter
def number_format_filter(num, symbol='￥'):
    return '{}{:,}'.format(symbol, num)

@profile
def print_receipt():

    # Create a new Jinja2 Environment and add the custom filter
    env = Environment()
    env.filters['ljust'] = ljust_filter
    env.filters['rjust'] = rjust_filter
    env.filters['number_format'] = number_format_filter
    env.filters['date_format'] = date_format_filter

    s = """\
    My Name:{{name}}
    伝票日付：{{ slipdate | date_format('%Y-%m-%d') }}
    伝票日付：{{ slipdate | date_format }}
    伝票番号：{{ slipno }}
    レジNO  ：{{ slipregno }}{% for item in items %}
    {{ item.name | truncate(10) | ljust(10) }} : {{item.price | number_format | rjust(10) }}{% endfor %}
    hogehoge
    """

    d = {'name': 'Mike',
        'slipdate': '2019-01-01',
        'slipno': '00123',
        'slipregno': '02' ,
        'items': [{'name': 'banana', 'price': 200},
                {'name': 'mango', 'price': 12800},
                {'name': 'apple', 'price': 4980}]}

    # Use the Jinja2 Environment to create a Template
    template = env.from_string(s)
    t = template.render(d)
    print(t)

if __name__ == "__main__":
    print_html()
    print_receipt()
