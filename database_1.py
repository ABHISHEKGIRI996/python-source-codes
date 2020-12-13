import sqlite3
db=sqlite3.connect('Abhi.db')
cursor=db.cursor()
cursor.execute('create table EMPPP (id integer,name text)')
#cursor.execute('drop table EMP')
id=1
name="abhishek"
cursor.execute('insert into EMPPP (id,name)values(?,?)',(id,name))
id=2
name="rahul"

cursor.execute('insert into EMPPP (id,name)values(?,?)',(id,name))
db.commit()
