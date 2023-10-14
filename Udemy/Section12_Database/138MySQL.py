# -*- coding: utf-8 -*-

import mysql.connector

mydb = None
mycursor = None
try:
    # MySQLに接続する
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="mydatabase"
    )

    # データを書き込む
    mycursor = mydb.cursor()

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


try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="mydatabase"
    )

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




