
# Section 12.Database

## SQLite
https://www.sqlite.org/index.html
### Windowsで必要なインストール
![代替テキスト](./Images/SQLiteSetup.png)

## MySQL
![代替テキスト](./Images/MySQLSetup1.png)
![代替テキスト](./Images/MySQLSetup2.png)
![代替テキスト](./Images/MySQLSetup3.png)
### Dockerでのインストール
```
# docker pull mysql:8.0.34
docker pull mysql:latest
mkdir my_mysql_data
# docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=password -d mysql:latest
docker run --name mysql-container `
  -e MYSQL_ROOT_PASSWORD=password `
  -v ${pwd}/my_mysql_data:/var/lib/mysql `
  -p 3306:3306 `
  -d mysql:latest
# 接続
docker exec -it mysql-container mysql -u root -p
# バージョン確認
SHOW VARIABLES LIKE "%version%";
# データベース一覧
show databases;
```
* Linux/Unix/MacOS: /etc/my.cnf または /etc/mysql/my.cnf
* Windows: C:\ProgramData\MySQL\MySQL Server 8.0\my.ini
```conf
# /etc/my.cnf
# この設定がなくても外部から接続できます。
[mysqld]
bind-address = 0.0.0.0
```
* MySQLの権限設定
```
create database mydatabase;
CREATE USER 'myuser'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'%';

GRANT ALL PRIVILEGES ON mydatabase.* TO 'root'@'%';
FLUSH PRIVILEGES;
```
# timeoutの確認
```
mysql> SHOW GLOBAL VARIABLES LIKE '%timeout%';
+-----------------------------------+----------+
| Variable_name                     | Value    |
+-----------------------------------+----------+
| connect_timeout                   | 10       |
| delayed_insert_timeout            | 300      |
| have_statement_timeout            | YES      |
| innodb_flush_log_at_timeout       | 1        |
| innodb_lock_wait_timeout          | 50       |
| innodb_rollback_on_timeout        | OFF      |
| interactive_timeout               | 28800    |
| lock_wait_timeout                 | 31536000 |
| mysqlx_connect_timeout            | 30       |
| mysqlx_idle_worker_thread_timeout | 60       |
| mysqlx_interactive_timeout        | 28800    |
| mysqlx_port_open_timeout          | 0        |
| mysqlx_read_timeout               | 30       |
| mysqlx_wait_timeout               | 28800    |
| mysqlx_write_timeout              | 60       |
| net_read_timeout                  | 30       |
| net_write_timeout                 | 60       |
| replica_net_timeout               | 60       |
| rpl_stop_replica_timeout          | 31536000 |
| rpl_stop_slave_timeout            | 31536000 |
| slave_net_timeout                 | 60       |
| ssl_session_cache_timeout         | 300      |
| wait_timeout                      | 28800    |
+-----------------------------------+----------+
23 rows in set (0.01 sec)
```

### Pythonの設定
```
# install mysql-connector-python
pip install mysql-connector-python==8.1.0
```


# SQL Alchemyを使う

```
pip install SQLAlchemy

pip install pymysql

```
# dbmを使う
## サーバ側の準備
https://github.com/kiyo7447/Local-Databases/tree/main/memcached
## 端末側の準備
```bash
pip install python-memcached
```
# TODO
