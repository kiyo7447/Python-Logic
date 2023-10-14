# -*- coding: utf-8 -*-

import mysql.connector

mydb = None
mycursor = None

def login_user():
    return mysql.connector.connect(
        host = "localhost",
        user= "myuser",
        password = "password",
        database = "mydatabase"
    )

def login_root():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )

def init_db():
    mydb = login_root()
    try:
        # データベース「mydatabase」がなければ作成する
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

        # ユーザ「myuser」を作成し、権限を付与する
        mycursor.execute("CREATE USER IF NOT EXISTS myuser@localhost IDENTIFIED BY 'password'")
        # mycursor.execute("GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'%'")
        # error:  1410 (42000): You are not allowed to create a user with GRANT
        # が発生するので、コメント化
        
        # データベース「mydatabase」へ切り替える
        mycursor.execute("USE mydatabase")

        # テーブルを作成する
        mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if mydb is not None and mydb.is_connected():
            if mycursor is not None:
                mycursor.close()
            mydb.close()
            print("MySQL connection is closed")


# MySQLに接続する
# 接続するデータベース「mydatabase」がなければ作成する
try:
    # MySQLに接続する
    # 接続するデータベース「mydatabase」がなければ作成する
    mydb = login_user()
except mysql.connector.Error as error:
    # 下記のエラーの場合は、ユーザ「myuser」が存在しない
    # Failed to connect to MySQL: 1045 (28000): Access denied for user 'myuser'@'172.17.0.1' (using password: YES)
    if error.errno == 1045:
        print("myuserでmydatabaseに接続に失敗したので、dbの初期化を始めます。error: {}".format(error))
        # データベース「mydatabase」を作成する
        init_db()
        # 再度、MySQLに接続する
        mydb = login_user()
finally:
    if mydb is not None and mydb.is_connected():
        if mycursor is not None:
            mycursor.close()
        mydb.close()
        print("MySQL connection is closed")

try:
    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(f"id={x[0]}, name={x[1]}, address={x[2]}")

    sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted.")

except mysql.connector.Error as error:
    print("Failed to insert record in MySQL: {}".format(error))

finally:
    if mydb is not None and mydb.is_connected():
        if mycursor is not None:
            mycursor.close()
        mydb.close()
        print("MySQL connection is closed")
