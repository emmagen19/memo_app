import time
user_text = input('Enter your text here: ')
trial = int(input('input countdown number in seconds: '))
limit = 0
while trial > limit:
    print(trial,)
    time.sleep(1)
    trial -= 1
print(f'**{user_text}**')