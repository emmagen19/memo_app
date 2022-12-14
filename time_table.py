print(f'welcome to the time table app')
user_name = input('what is your name: ')
user_number = int(input('please enter your number: '))
print(f'{user_name}, your time table is:')
for a in range(1,11):
    print(f'{user_number} x {a} = {a*user_number}')
print(f'Thank you!!\nTry again')