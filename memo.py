import time

db = ['python', 'java', 'c++', 'html']


def main():
    print('Welcome to memo, Choose\n1 to add memo\n2 to edit memo\n3 to read memo\n4 to delete memo\n5 to quit memo')
    user_input = int(input('Enter a number: '))
    if user_input == 1:
        add_memo()
    elif user_input == 2:
        edit_memo()
    elif user_input == 3:
        read_memo()
    elif user_input == 4:
        delete_memo()
    elif user_input == 5:
        print('Quiting Program')
        time.sleep(1)
        quit()


def add_memo():
    print('Type your memo')
    user_memo = input('')
    db.append(user_memo)
    print('memo successfully added')
    print('Returning to menu')
    time.sleep(1)
    main()


def edit_memo():
    print(db)
    print('Enter the number of the memo you wish to change')
    input_1 = int(input(''))
    print(db[input_1-1])
    print('Enter what you want to edit it with')
    input_2 = input('')
    print(f'Are you sure you want to edit {db[input_1-1]} with {input_2}')
    print('Enter y to confirm or n to return to main menu')
    input_3 = input(' ')
    if input_3 == "y":
        db[input_1-1] = input_2
        print('Memo has been successfully edited')
        print('Returning to menu')
        time.sleep(1)
        main()
    elif input_3 == 'n':
        print('Returning to menu')
        time.sleep(1)
        main()
    else:
        print('Wrong Input')
        edit_memo()


def read_memo():
    print("Enter y to read memo \n      n to return to main menu")
    user_input = (input('Y/N: '))
    if user_input == "y":
        print(f'your memo is \n{db}')
        print('Returning to main menu')
        time.sleep(1)
        main()
    elif user_input == "n":
        print('Returning to main menu')
        time.sleep(1)
        main()
    else:
        print('Wrong Input')
        read_memo()

def delete_memo():
    print(db)
    print('Enter the number of the memo you wish to delete')
    input_1 = int(input(""))
    print(f'Are you sure you want to delete {db[input_1-1]}')
    print('Enter y to confirm or n to return to main menu')
    input_2 = input('')
    if input_2 == "y":
        db.pop(input_1-1)
        print("memo deleted successfully")
        print('Returning to main menu')
        time.sleep(1)
        main()
    elif input_2 == 'n':
        print('Returning to main menu')
        time.sleep(1)
        main()
    else:
        print('Wrong Input')
        delete_memo()

main()




    


