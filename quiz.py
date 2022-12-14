score = []
user_name = input('Enter your name:')
correct_ans = ['**********************************************\nYou got these questions right!!\n**********************************************']
wrong_ans = ['\n**********************************************\nYou failed these questions\n**********************************************']
def menu():
    print(f"Welcome {user_name} to the Quiz game\nTest your knowlegde on Nigeria's history and facts")
    print('There are 10 questions in total, Good luck!')
    question_1()

    
def question_1():
    print('Question 1')
    print(f'When did Nigeria gain its Independence?\n(a) 1950\n(b) 1960\n(c) 1970\n(d) 1980')
    user_input = input('Select one option:')
    if user_input == 'b':
        print('Correct!!!')
        score.append(1)
        correct_ans.append(f' \nWhen did Nigeria gain its Independence?')
        question_2()
    else:
        print('wrong answer\nb was correct')
        wrong_ans.append(f' \nWhen did Nigeria gain its Independence?\nAns = 1960')
        question_2()


def question_2():
    print('Question 2')
    print('How many states are in Nigeria?\n(a) 33\n(b) 34\n(c) 35\n(d) 36')
    user_input = input('Select one option:')
    if user_input == 'd':
        print('Correct!!!')
        score.append(1)
        correct_ans.append(f'\nHow many states are in Nigeria?')
        question_3()
    else:
        print("wrong answer\nd was correct")
        wrong_ans.append(f'\nHow many states are in Nigeria?\nAns = 36')
        question_3()


def question_3():
    print('Question 3')
    print("What are the three main tribes in Nigeria?")
    print("(a) zulu, tiv, esan\n(b) Igbo, Yoruba, Hausa\n(c) ijaw, mbasi, ekasi\n(d) benin, uhrobo, ewu")
    user_input = input('Select one option:')
    if user_input == 'b':
        print('Correct!!!')
        score.append(1)
        correct_ans.append(f' \nWhat are the three main tribes in Nigeria?')
        question_4()
    else:
        print("wrong answer\nb was correct")
        wrong_ans.append(f'\nWhat are the three main tribes in Nigeria?\nAns =  Igbo, Yoruba, Hausa')
        question_4()


def question_4():
    print('Question 4')
    print('What state is considered the heartbeat of the nation?\n(a)Edo state\n(b)Imo state\n(c)Ebonyi state\n(d)Lagos state')
    user_input = input('select one option:')
    if user_input == 'a':
        print('correct!!!')
        score.append(1)
        correct_ans.append(f'\nWhat state is considered the heartbeat of the nation?')
        question_5()
    else:
        print("wrong answer\na was correct")
        wrong_ans.append(f'\nWhat state is considered the heartbeat of the nation?\nAns = Edo state')
        question_5()


def question_5():
    print('Question 5')
    print('Chappal Waddi is the highest mountain of Nigeria. What state is it located in?')
    print('(a) Edo\n(b) Abia\n(c) taraba\n(d) Ebonyi')
    user_input = input('Select one option:')
    if user_input == 'c':
        print('Correct!!!')
        score.append(1)
        correct_ans.append(f'\nChappal Waddi is the highest mountain of Nigeria. What state is it located in?')
        question_6()
    else:
        print('wrong answer\nc was correct')
        wrong_ans.append(f'\nChappal Waddi is the highest mountain of Nigeria. What state is it located in?\nAns = Taraba state')
        question_6()


def question_6():
    print('Question 6')
    print('Nigeria is divided into 36 states. Which one is the largest by area?')
    print('(a) adamawa\n(b) niger\n(c) zamfara\n(d) kwara')
    user_input = input('Select one option:')
    if user_input == 'b':
        print('Correct!!!')
        score.append(1)
        correct_ans.append(f'\nNigeria is divided into 36 states. Which one is the largest by area?')
        question_7()
    else:
        print('wrong answer\nb was correct')
        wrong_ans.append(f'\nNigeria is divided into 36 states. Which one is the largest by area?\nAns = Niger state')
        question_7()


def question_7():
    print('Question 7')
    print("What was General Babangida's position before becoming president?")
    print('(a) Major General\n(b) leuitenant\n(c) leuitenant Colonel\n(d) Cheif of army staff')
    user_input = input('Select one option:')
    if user_input == 'd':
        print('Correct!!!')
        score.append(1)
        correct_ans.append(f"\nWhat was General Babangida's position before becoming president?")
        question_8()
    else:
        print('wrong answer\nd was correct')
        wrong_ans.append(f"\nWhat was General Babangida's position before becoming president?\nAns = Cheif of army staff")
        question_8()


def question_8():
    print('Question 8')
    print('Nigeria is a little over twice the size of what US state?\n(a) Texas\n(b) Washingnton DC\n(c) Califonia\n(d) New-york')
    user_input = input('Select one option:')
    if user_input == 'c':
        print('Correct!!!')
        score.append(1)
        correct_ans.append(f'\nNigeria is a little over twice the size of what US state?')
        question_9()
    else:
        print('wrong answer\nc was correct')
        wrong_ans.append(f'\nNigeria is a little over twice the size of what US state?\nAns = Califonia')
        question_9()


def question_9():
    print('Question 9')
    print('Nigerians Wole Soyinka, Ben Okri and Chinua Achebe have all achieved renown in which field?')
    print('(a) Music\n(b) theatre\n(c) Architecture\n(d) Literature')
    user_input = input('Select one option:')
    if user_input == 'd':
        print("Corrrect!!!")
        score.append(1)
        correct_ans.append(f'\nNigerians Wole Soyinka, Ben Okri and Chinua Achebe have all achieved renown in which field?')
        question_10()
    else:
        print('wrong answer\nd was correct')
        wrong_ans.append(f'\nNigerians Wole Soyinka, Ben Okri and Chinua Achebe have all achieved renown in which field?\nAns = Literature')
        question_10()


def question_10():
    print('Question 10')
    print('Zuma Rock is situated near what Nigerian city?\n(a) Abuja\n(b) Abeokuta\n(c) yenegua\n(d) Oshogbo')
    user_input = input('Select one option:')
    if user_input == 'a':
        print("correct!!!")
        score.append(1)
        correct_ans.append(f'\nZuma Rock is situated near what Nigerian city?')
    else:
        print("wrong answer\na was correct")
        wrong_ans.append(f'\nZuma Rock is situated near what Nigerian city?\nAns = Abuja')
    print(f'***Quiz finished***\nYou scored {sum(score)}/10')
    
menu()
script = open(f'{user_name}.txt', 'w')
script.writelines(correct_ans)
script.close()
script = open(f'{user_name}.txt','a')
script.writelines(wrong_ans)
script.close()


