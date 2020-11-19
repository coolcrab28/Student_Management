import sqlite3
from prettytable import from_db_cursor
import os

conn = sqlite3.connect('students.db')
c = conn.cursor()

msg = """
Choose An Option:
1 : Show Current Data
2 : Insert Data
3 : Delete Data
4 : Update Data
0 : Exit
"""
def show():
    a = c.execute("""
    SELECT * FROM students;
    """)
    mytable = from_db_cursor(a)
    print(mytable)

def clear():
    os.system('cls')