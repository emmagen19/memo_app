from tkinter import *

root = Tk()
title = 'Mutiplication Table'
title_ = Label(root, text= title)
title_.grid(row=0, column=0)
num = int(input('Enter your number: '))
for x in range(1, 13):
    result = (f'{num} x {x}={num*x}')
    out = Label(root, text= result)
    out.grid(row=x,column=0)
x = 2+2
print(x)



root.mainloop()