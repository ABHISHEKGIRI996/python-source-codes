#database manupulation

import sqlite3

db=sqlite3.connect('final.db')
cursor=db.cursor()

cursor.execute('create table student(s_no integer, name text, city text, class integer, age integer)')

cursor.execute('insert into student(s_no,name,city,class,age)\
                values(1,"Abhishek","Delhi",12,20)');
cursor.execute('insert into student(s_no,name,city,class,age)\
                values(2,"Deepak","Chirag Delhi",11,22)');
cursor.execute('insert into student(s_no,name,city,class,age)\
                values(3,"Ravi","Faridabad",12,23)');
cursor.execute('insert into student(s_no,name,city,class,age)\
                values(4,"Aman","New Delhi",10,21)');
cursor.execute('insert into student(s_no,name,city,class,age)\
                values(5,"Riya","Rohini",12,21)');
cursor.execute('insert into student(s_no,name,city,class,age)\
                values(6,"Dilip","Delhi",11,24)');

#read from (SELECT)databse table

print("read from (SELECT)databse table")
cursor.execute('select * from student')
al=cursor.fetchall()
for row in al:
    print(row)

print()

for row in al:
    print("{0}:{1}:{2}:{3}:{4}".format(row[0],row[1],row[2],row[3],row[4]))

#select single record from table
print("select single record from table")
cursor.execute('select * from student')
sr=cursor.fetchall()
print(sr[3])
print()
#select single record from table in a loop
print("select single record from table in a loop")
for i in range(0,6):
    print(sr[i])



#use of where clause
print("which data you want to fetch ")
ft=input()
s_no=ft
#f=chr(ft)
ftt = ('select * from student where s_no ='+ft)

cursor.execute(ftt)
al=cursor.fetchall()
for row in al:
    print("{0} | {1} | {2} | {3} | {4}".format(row[0],row[1],row[2],row[3],row[4]))


#update command
print("In which attribute you want to update (s_no,name,city,class,age)")
att=input()
print("what data you want to update ")
data=input()
print("Where you want to update ")
up=input()

exe='update student set '+att+'="'+data+'"''where s_no = '+up
cursor.execute(exe)

print("after update \n ")
cursor.execute('select * from student')
al=cursor.fetchall()
for row in al:
    print(row)


# delete command

print(" delete command (s_no = 4 is deleting)") 


cursor.execute('delete from student\
                where s_no = 4');

cursor.execute("select * from student")
al=cursor.fetchall()
for row in al:
    print("{0} {1} {2} {3} {4}".format(row[0],row[1],row[2],row[3],row[4]))

# table deleted

cursor.execute('drop table student')
db.commit()
        





