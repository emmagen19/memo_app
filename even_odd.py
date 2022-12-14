def even_nums():
    print(f'Even numbers from 1-100 are:')
    x = [y for y in range(2,102,2)]
    print(x)
def odd_nums():
    print(f'Odd numbers from 1-100 are:')
    x = [y for y in range(1,100,2)]
    print(x)
def prime_nums():
    y =[]
    print(f'Prime numbers from 1-100 are:')
    for x in range(2,100):
        if x%2 == 0:
            continue
        y.append(x)
    print(y)
        
prime_nums()