import sqlite3
from prettytable import from_db_cursor
import sys
conn = sqlite3.connect('students.db')

c = conn.cursor()
# c.execute("""
# CREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(30),age INTEGER )
# """)
try:
    name = sys.argv[1]
    age = sys.argv[2]
except:
    print("An error occured!")
    exit()

try:
    c.execute(f"""
    INSERT INTO students(name,age) VALUES('{name}', {age});
    """)
except sqlite3.Error as er:
    print('SQLite error: %s' % (' '.join(er.args)))


conn.commit()

a = c.execute("""
SELECT * FROM students;
""")
mytable = from_db_cursor(a)
print(mytable)
c.close()