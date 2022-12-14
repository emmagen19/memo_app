import random
print(f'Welcome to the guessing game')
user_name = input('What is your name?: ')
user_stake = input('How much do you want to stake $: ')
user_guess = input('Enter your number(1-5): ')
com_guess = random.randrange(1, 6)
com_guess_log = []
com_guess_log.append(com_guess)
user_winnings = int(user_stake)
user_losses = int(user_stake)/3
if int(user_guess) == com_guess and int(user_stake) <= 1000:
    print(f'Congratulations {user_name}, you won ${int(user_winnings)*2}')
elif int(user_guess) == com_guess and int(user_stake) <= 2000:
        user_winnings = int(user_stake)*4
        print(f'Congratulations {user_name}, you won ${user_winnings}')
elif int(user_guess) == com_guess and int(user_stake) <= 3000:
        user_winnings = int(user_stake)*5
        print(f'Congratulations {user_name}, you won ${user_winnings}')
elif int(user_guess) == com_guess  and  int(user_stake) <= 4000:
        user_winnings = int(user_stake)*6
        print(f'Congratulations {user_name}, you won ${user_winnings}')
elif int(user_guess) == com_guess and int(user_stake) <= 5000:
        user_winnings = int(user_stake)*7
        print(f'Congratulations {user_name}, you won ${user_winnings}')
elif int(user_guess) == com_guess and int(user_stake) > 5000:
        user_winnings = int(user_stake)*10
        print(f'Congratulations {user_name}, you won ${user_winnings}')
else:
    print(f'sorry {user_name}, the winning number was {com_guess}')
    print(f'you lost ${int(user_losses)}')
print(f'The previous winning number was {com_guess_log}')
print(f'Have another go!!')


