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