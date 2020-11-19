from modules import *
clear()
while True:
    print(msg)
    choice = int(input("Enter : "))
    if choice == 1:
        clear()
        show()
    elif choice == 0:
        clear()
        break
        exit()
    elif choice == 2:
        clear()
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        os.system(f'python input.py "{name}" {age}')

