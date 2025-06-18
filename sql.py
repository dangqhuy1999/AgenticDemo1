import sqlite3

connection = sqlite3.connect("student.db")

#cursor
cursor=connection.cursor()

'''
# Liệt kê các bảng có trong DB
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in DB:", tables)

input("___")
'''
# Create table

table_info="""
Create table IF NOT EXISTS STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

## Insert some more records 

cursor.execute('''Insert Into STUDENT values('huydang', 'genai', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('huydang2', 'Dgenai', 'B', 91)''')
cursor.execute('''Insert Into STUDENT values('huydan3', 'genai', 'C', 55)''')
cursor.execute('''Insert Into STUDENT values('huydang4', 'powerbi', 'A', 78)''')
cursor.execute('''Insert Into STUDENT values('huydang5', 'Data Science', 'D', 91)''')

## Dispaly all the records

print("The insert records are")

data =cursor.execute('''Select * from STUDENT''')
for row in data: 
    print(row)

## Commit your changes in the database 

connection.commit()
connection.close()
