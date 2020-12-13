#database management
import sqlite3
db=sqlite3.connect('Abhi.db')
cursor=db.cursor()
cursor.execute(insert into EMP(id,name)\
                values(4,"ravi"));
cursor.execute('insert into EMP(id,name)\
                values(5,"savi")');
db.commit()

