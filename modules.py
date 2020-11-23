import sqlite3
import re 
from prettytable import from_db_cursor
import os
import time
import uuid


conn = sqlite3.connect('students.db')
c = conn.cursor()
cr = """
CREATE TABLE IF NOT EXISTS students(id VARCHAR(20) PRIMARY KEY NOT NULL,
    name VARCHAR(30) NOT NULL,
    age INTEGER NOT NULL,
    email VARCHAR(40) NOT NULL
    )
"""
c.execute(cr)

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
    c = conn.cursor()
    try:
        i = (str(uuid.uuid4())[0:8])
        n = input("Enter YES to confirm : ")
        if n.lower() == 'yes' or n.lower == 'y':
            c.execute(f"""
            INSERT INTO students(id,name,age,email) VALUES('{i}','{name}', {age}, '{email}');
            """)
            conn.commit()
            clear()
            show()
            c.close()
        else:
            conn.rollback()
            print("No changes were made..")

    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        show()
    
    

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
        
def create_table():
    c = conn.cursor()
    clear()
    st = """
    CREATE TABLE students(id VARCHAR(20) PRIMARY KEY NOT NULL,
    name VARCHAR(30) NOT NULL,
    age INTEGER NOT NULL,
    email VARCHAR(40) NOT NULL
    )
    """
    c.execute(st)


def remove():
    clear()
    show()
    i = (input("Enter ID to remove: "))
    c.execute(f"""SELECT name FROM students WHERE id = '{i}' """)
    rows = c.fetchall()
    name = rows[0][0]
    clear()
    print(f"""Are you sure you want to remove '{name}' from the table? (y/N)""")
    ch = input()
    if not(ch):
        print("No changes were made.")
    elif ch.lower() == 'y' or ch.lower() == 'yes':
        print("OK...."); 
        ct = f"""DELETE FROM students WHERE id ='{i}' """
        c.execute(ct)
        conn.commit()
        print('Done!')
        time.sleep(1)
        clear()
        show()

def update():
    clear()
    show()
    i = (input("Enter ID of Student to update: "))
    c.execute(f"""SELECT name FROM students WHERE id = {i} """)
    rows = c.fetchall()
    name = rows[0][0]
    print(name)

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
            remove()
        elif choice == 4:
            clear()
            update()
        elif choice == 999999:
            clear()
            destroy()

def start():
    clear()
    main()

# start()