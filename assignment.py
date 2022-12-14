def program_1():
    try:
        user_input = int(input(":"))
        user_input1 = int(input(':'))
    except ValueError:
        print('Input must be integer')
        program_1()
    


def program_2():
    try:
        user_input = int(input(":"))
        user_input1 = int(input(':'))
    except ValueError:
        print('must be integer')
        program_2()
    finally:
        print(user_input+user_input1)

def program_3():
    try:
        user_input = int(input(":"))
        user_input1 = int(input(':'))
    except ValueError:
        print('Input must be integer')
        program_3()
    else:
        print('code is good to go')

def program_4():
    try:
        user_input = int(input(":"))    
    except ValueError:
        print('Input must be integer')
        program_3()
    except:
 
        print('something else went wrong')
program_4()