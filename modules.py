import sqlite3
import re 
from prettytable import from_db_cursor
import os

conn = sqlite3.connect('students.db')
c = conn.cursor()

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

msg = """
Choose An Option:
1 : Show Current Data
2 : Insert Data
3 : Delete Data
4 : Update Data
0 : Exit
"""
def show():
    c
    a = c.execute("""
    SELECT * FROM students;
    """)
    mytable = from_db_cursor(a)
    print(mytable)

def clear():
    os.system('cls')

def inp(name,age,email):
    c
    try:
        c.execute(f"""
        INSERT INTO students(name,age,email) VALUES('{name}', {age}, '{email}');
        """)
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
    n = input("Enter YES to confirm : ")
    if n == "YES" or n == "yes":
        conn.commit()
        a = c.execute("""
        SELECT * FROM students;
        """)
        mytable = from_db_cursor(a)
        print(mytable)
        c.close()
    else:
        print("No changes were made..")
        c.close()


def check(email):  
    if(re.search(regex,email)):  
        return True
          
    else:  
        return False
      