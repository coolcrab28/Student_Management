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

999999 : Clear all data
0 : Exit
"""
def show():
    c = conn.cursor()
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
        clear()
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
def destroy():
    print("Doing this will delete all the data. \nAre you sure you want to continue?")
    n = input("""Enter 'CONFIRM' : """)
    if n == 'CONFIRM':
        c = conn.cursor()
        st = """DROP TABLE students"""
        c.execute(st)
        conn.commit()
        c.close()
        create_table()
        show()
    else:
        print("Abort!")
        c.close()
def create_table():
    c = conn.cursor()
    clear()
    st = """
    CREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(30) NOT NULL,
    age INTEGER NOT NULL,
    email VARCHAR(40) NOT NULL
    )
    """
    c.execute(st)

def main():
    while True:
        print(msg)
        choice = int(input("Enter : "))
        if choice == 1:
            clear()
            show()
        elif choice == 0:
            c.close()
            clear()
            exit()
        elif choice == 2:
            clear()
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            print("validating email....")
            a = check(email)
            if (a):
                inp(name,age,email)
            else:
                print("Invalid email format!")
        elif choice == 3:
            clear()
        elif choice == 4:
            clear()
        elif choice == 999999:
            clear()
            destroy()
        