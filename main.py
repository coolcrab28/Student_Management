from modules import *
clear()
while True:
    print(msg)
    choice = int(input("Enter : "))
    if choice == 1:
        clear()
        show()
    elif choice == 0:
        c.close()
        clear()
        break
        exit()
    elif choice == 2:
        clear()
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        inp(name,age)
        