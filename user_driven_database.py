#database management user-driven

import sqlite3

def database:
    print("\n     DATA BASE MANAGEMENT    \n")
    print("Want to create your own databse (y/n)")
    ch=input()
    if (ch=="Y") or (ch=="y"):
        d_base=input("Enter your databsae name : ")
        d_base=d_base+'.db'
        db=sqlite3.connect(d_base)
    else:
        print("A default database is created ")
    d_base='default.db'
    db=sqlite3.connect(d_base)
    cursor=db.cursor()

    print("Want to create table (y/n)")
    ch=input()
    if (ch=="Y") or (ch=="y"):
        table=input("Enter your Table name : ")
        n_table='create table '+table+'(S_no integer)'
        
        cursor.execute(n_table)
        print("table is created with default attribute S_no ")
    else:
        table='deafult'
        n_table='create table '+table+'(S_no integer)'
        cursor.execute(n_table)
    print("\n Insertion of data ")
    print("How many attributes you want : ")
    n=int(input())
    s=[]
    for i in range(0,n):
        s1=input("Enter your attribute name and data type : ")
        s.append(s1)
        d_type=input()
        n_att='alter table '+table+ ' add '+s[i]+' '+d_type
        
        cursor.execute(n_att)
    #for i in range(0,n):
    #for i in range(0,n):
        #if i==n-1:
    #insert='insert into '+table+' ('+','.join(s)+')values(' + ','.join(['?'] * n+1)+')'
    #print(insert)
    db.commit()




    

