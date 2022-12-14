name = 'bob'
def question():
    global name
    name = name.__add__( 'daniel')
    q2()
    
def q2():
    global name
    name = name.__add__( 'amaka')
    print(name)
go = 'holiday'
go = go.__add__(' beans')
go = go.__add__('\napples')
question()
