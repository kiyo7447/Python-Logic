# pip install flask
from flask import Flask
from flask import g # global値管理
from flask import render_template
from flask import request
from flask import Response

import sqlite3

import json

app = Flask(__name__)

# テンプレートフォルダを変更することも可能
#app = Flask(__name__, template_folder='templates')

# ルーティング
@app.route('/')
@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hello2')
def hello2():
    return 'Hello2, World!'

@app.route('/getuser/<int:id>')
def getuser(id):
    return f"getuser: {id}"

@app.route('/hello/<string:name>')
def hello_name(name):
    return f"Hello, {name}!"

@app.route('/hellotemplate/<string:name>')
def hello_template(name):
    return render_template('157Flask.html', name=name, title='Hello Template')

@app.route('/hellotemplate')
@app.route('/hellotemplate2/<string:name>')
def hello_template2(name=None):
    return render_template('157Flask.html', name=None, title='Hello Template2')

# Put
# @app.route('/post', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    print(f"request.method: {request.method}")
    return str(request.values['username'])

# databaseを使う
# Flaskのドキュメントにあるコード
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        # db = g._database = sqlite3.connect('test_sqlite.db')
        db = g._database = sqlite3.connect('157Flask.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()
    curs.execute(
        'CREATE TABLE IF NOT EXISTS persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )
    name = request.values.get('name', name)
    if request.method == "GET":
        curs.execute('SELECT * FROM persons WHERE name = "{}"'.format(name))
        person = curs.fetchone()
        if not person:
            return "No", 404
        user_id, name = person
        return "name: {}, id: {}".format(name, user_id), 200# 200: OK
    if request.method == "POST":
        curs.execute('INSERT INTO persons(name) values("{}")'.format(name))
        db.commit()
        return "created {}".format(name), 201# 201: created
    if request.method == "PUT":
        new_name = request.values['new_name']
        curs.execute('UPDATE persons set name = "{}" WHERE name = "{}"'.format(new_name, name))
        db.commit()
        return "updated {}: {}".format(name, new_name), 200
    if request.method == "DELETE":
        c = curs.execute('DELETE from persons WHERE name = "{}"'.format(name)).rowcount
        db.commit()
        return "deleted {}, count {}".format(name, c), 200
    curs.close()

@app.route('/employees')
def employees():
    db = get_db()
    curs = db.cursor()
    curs.execute('SELECT * FROM persons')
    persons = curs.fetchall()
    curs.close()
    # persionsをjsonで返す
    return Response(
        # json.dumps(persons),
        # mimetype='application/json',
        # jsonを整形して返す
        json.dumps(persons, indent=2),
        mimetype='application/json',
    )


def main():
    app.debug = True
    # default port is 5000
    #app.run()
    app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    main()


"""
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
これは、現在のサーバーが開発用であり、本番環境で使用するべきではないという警告です。本番環境では、WSGIサーバー（例：Gunicorn、uWSGI）を使用することが推奨されています。

# この仕組みではブラウザの自動リロードには対応していません。
import webbrowser
webbrowser.open('http://127.0.0.1:5000'/hello/hoge)

"""