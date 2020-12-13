import csv
import sqlite3

#Give the table a name and use it for the file as well
table_name = 'Example'
a = open(table_name + '.csv', 'r')

#Use a dict reader
my_reader = csv.DictReader(a)
print( my_reader.fieldnames )# Use this to create table and get number of field values,etc.

# create statement
create_sql = 'CREATE TABLE ' + table_name + '(' + ','.join(my_reader.fieldnames) + ')'
print (create_sql)

#open the db
conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table using field names
c.execute(create_sql)
insert_sql = 'insert into ' + table_name + ' (' + ','.join(my_reader.fieldnames) + ') VALUES (' + ','.join(['?'] * len(my_reader.fieldnames))+ ')'
print (insert_sql)

values = []
for row in my_reader:
    row_values = []
    for field in my_reader.fieldnames:
        row_values.append(row[field])
    values.append(row_values)

c.executemany(insert_sql, values)
