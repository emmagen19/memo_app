import random
print(f'welcome to the betting game!!')
user_name = input('what is your name?: ')
user_stake = int(input('place your bet: '))
user_guess1 = int(input('Enter your 1st number: '))
user_guess2 = int(input('Enter your 2nd number: '))
user_guess3 = int(input('Enter your 3rd number: '))
user_log = []
user_log.append(user_guess1)
user_log.append(user_guess2)
user_log.append(user_guess3)
com_guess1 = random.randrange(1,6)
com_guess2 = random.randrange(1,6)
com_guess3 = random.randrange(1,6)
com_log = []
com_log.append(com_guess1)
com_log.append(com_guess2)
com_log.append(com_guess3)
user_winnngs = user_stake*2
user_losses = user_stake/2
if user_stake <= 2000:
    user_winnngs = user_stake*2.5
elif user_stake <= 5000:
    user_winnngs = user_stake*3
elif user_stake > 5000:
    user_winnngs = user_stake*3.5
else:
    user_winnngs = user_stake*2
if user_log == com_log:
    user_winnngs = user_stake*5
    print(f'You hit the jackpot!!!\n your winnings are ${user_winnngs} ')
elif user_guess1 == com_guess1 and user_guess1 == com_guess2 or user_guess1 == com_guess1 and user_guess1 == com_guess3 or user_guess1 == com_guess2 and user_guess1 == com_guess3:
    user_winnngs = user_stake*2.5
    print(f'Congrats {user_name}, you won {user_winnngs}')
elif user_guess2 == com_guess1 and user_guess2 == com_guess2 or user_guess2 == com_guess1 and user_guess2 == com_guess3 or user_guess2 == com_guess2 and user_guess2 == com_guess3:
    user_winnngs = user_stake*2.5
    print(f'Congrats {user_name}, you won {user_winnngs}')
elif user_guess3 == com_guess1 and user_guess3 == com_guess2 or user_guess3 == com_guess1 and user_guess3 == com_guess3 or user_guess3 == com_guess2 and user_guess3 == com_guess3:
    user_winnngs = user_stake*2.5
    print(f'Congrats {user_name}, you won {user_winnngs}')
elif user_guess1 == com_guess1 or user_guess1 == com_guess2 or user_guess1 == com_guess3:
    print(f'Congrats {user_name}, you won {user_winnngs}')
elif user_guess2 == com_guess1 or user_guess2 == com_guess2 or user_guess2 == com_guess3:
    print(f'Congrats {user_name}, you won {user_winnngs}')
elif user_guess3 == com_guess1 or user_guess3 == com_guess2 or user_guess3 == com_guess3:
    print(f'Congrats {user_name}, you won {user_winnngs}')
else:
    print(f'Sorry {user_name},you lost {user_losses}')
print(f'Winning numbers: {com_log}\n Your numbers: {user_log}')
print("Try Again!!")
