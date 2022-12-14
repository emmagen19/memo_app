from pathlib import Path
from accounts import accreditation

def card():
    accreditation()

def edit():
    #accreditation()
    #if accreditation:
        #print('Kindly modify your card details')
    db = []
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    mobile_number= input('Mobile_number: ')
    email = input('Email: ')
    password = input('Password: ')
    file = open(f'C:/Users/user/Desktop/work place/python/inec/accounts{email}.txt','w')
    data = [f'Thanks for your registration\n Name: {first_name}, \n Last Name: {last_name}, \n Mobile-Number: {mobile_number}, \n Email : {email}, \n Password: {password}']
    for i in range(len(data)):
        db.append(data[i])
    file.writelines(db)
    print(f'Your details have been successfully updated')




