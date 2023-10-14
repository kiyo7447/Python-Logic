# -*- coding: utf-8 -*-
# SQLAlchemy（SQLアルカミー）を使ってみる

import sqlalchemy 
import sqlalchemy.orm 
# import sqlalchemy.ext.declarative
# Ver2.0へ対応
from sqlalchemy.orm import declarative_base

print(sqlalchemy.__version__)
# 2.0.21

# echo=Trueで実行時のSQLを出力する

#sqliteのメモリエンジンを用意する
# SQLiteのメモリエンジンを用意する

#engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=False)
# SQLiteのファイルエンジンを用意する
#engine = sqlalchemy.create_engine('sqlite:///Session11_139SQLAlchemy.db', echo=False)

# MySQLのエンジンを用意する
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost:3306/mydatabase', echo=False)

# Baseを用意する
#Base = sqlalchemy.ext.declarative.declarative_base()
# ↓ Ver2.0へ対応
Base = declarative_base()

# Persionクラスを用意する。
class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))
    age = sqlalchemy.Column(sqlalchemy.Integer)

Base.metadata.create_all(engine)

# INSERT
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name='Joe Higashi', age=20)
session.add(p1)
p2 = Person(name='Duck King', age=15)
session.add(p2)
p3 = Person(name='Tung Fu Rue', age=77)
session.add(p3)

session.commit()

# SELECT ROWS
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name, person.age)

# SELECT ROW
person = session.query(Person).filter_by(name='Duck King').first()
print(person.id, person.name, person.age)
print(f"person.name = {person.name}, person.age = {person.age}, person.id = {person.id}")
