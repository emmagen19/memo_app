from pathlib import Path
def signup():
    print('Welcome to 2022 INEC Voters continuos registration\n Create a Portal Account to Continue.')
    db = []
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    mobile_number= input('Mobile_number: ')
    email = input('Email: ')
    password = input('Password: ')
    file = open(f'accounts/{email}.txt','a')
    data = [f'Thanks for your registration\n Name: {first_name}, \n Last Name: {last_name}, \n Mobile-Number: {mobile_number}, \n Email : {email}, \n Password: {password}']
    for i in range(len(data)):
        db.append(data[i])
    file.writelines(db)

def accreditation():
    print('Welcome to 2022 INEC Voters continuos registration.\nLog in here if you already have a Portal Account ')
    email = input('Email: ')
    password = input('Password: ')

    entries = Path('accounts/')
    
    email_ = f'{email}.txt'
    
    _db = []
    for entry in entries.iterdir():
        _db.append(entry.name)
    
    if email_ in _db:
        print('++++++++ Congratulations! ++++++++\n Here are your details')
        f = open(entries/email_,'r')
        print('******************************')
        print(f.read())
        print('******************************')
        f.close()
    else:
        print("Invalid users detected!!!")


   
    



   
        



