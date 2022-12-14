import random
print('welcome to the guessing name 2.0!')
user_name = input('what is your name: ')
com_log = []
user_log = []
total_log_winnings = []
total_log_losses = []
guess_limit = 4
trial = 1

while trial < guess_limit:
    lives = trial
    user_stake = int(input('how much do you want to stake$?: '))
    user_guess = int(input('please enter your number(1-5): '))
    user_winnings = int(user_stake)*2
    user_losses = int(user_stake)/2
    user_log.append(int(user_guess))
    com_guess = random.randrange(1,6)
    com_log.append(com_guess)
    if user_guess == com_guess and int(user_stake) <= 1000:
        print(f'congratutions {user_name}, you won {user_winnings}')
        print(f'you have used {lives} lives')
        user_losses = 0
    elif user_guess == com_guess and int(user_stake) <= 2000:
            user_winnings = int(user_stake)*3
            print(f'congratutions {user_name}, you won {user_winnings}')
            print(f'you have used {lives} lives')
            user_losses = 0
    elif user_guess == com_guess and int(user_stake) <= 3000:
            user_winnings = int(user_stake)*4
            print(f'congratutions {user_name}, you won {user_winnings}')
            print(f'you have used {lives} lives')
            user_losses = 0  
    elif user_guess == com_guess and int(user_stake) <= 4000:
            user_winnings = int(user_stake)*5
            print(f'congratutions {user_name}, you won {user_winnings}')
            print(f'you have used {lives} lives')
            user_losses = 0 
    elif user_guess == com_guess and int(user_stake) >= 5000:
            user_winnings = int(user_stake)*6
            print(f'congratutions {user_name}, you won {user_winnings}')
            print(f'you have used {lives} lives')
            user_losses = 0             
    else:
        print(f'Oops {user_name}, you lost {user_losses}')
        print(f'you have used {lives} lives')
        user_winnings = 0
    total_log_losses.append(user_losses)
    total_log_winnings.append(user_winnings)
    trial += 1

print(f'Computer number: {com_log}\n User guesses: {user_log}')
total_wins = sum(total_log_winnings) 
total_lost = sum(total_log_losses)
total_cash =  sum(total_log_winnings) -  sum(total_log_losses) 
if total_cash == -sum(total_log_winnings) -  sum(total_log_losses):
    total_cash = 0
    print(f'your winnings: {total_wins} \n your losses: {total_lost} \n your cash$: {total_cash}')
else:
    print(f'your winnings: {total_wins} \n your losses: {total_lost} \n your cash$: {total_cash}')

