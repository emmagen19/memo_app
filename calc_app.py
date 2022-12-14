from tkinter import *
root =  Tk()
root.geometry("500x350")
root.title('Calculator')
e = Entry(root, width=60, borderwidth=10)
e.grid(row=0,column=0,columnspan=4)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def button_minus():
    first_number = e.get()
    global f_num
    global math
    math = 'minus'
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'divide'
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiply'
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "minus":
        e.insert(0, f_num - int(second_number))
    elif math == 'divide':
        e.insert(0, f_num/int(second_number))
    elif math == 'multiply':
        e.insert(0, f_num*int(second_number))



zero_btn = Button(root, text=0,padx=40, pady=20, command=lambda: button_click(0)).grid(row=5, column=0)
one_btn = Button(root, text=1,padx=40, pady=20,command=lambda: button_click(1)).grid(row=4,column=0)
two_btn = Button(root, text=2,padx=40, pady=20, command=lambda: button_click(2)).grid(row=4, column=1)
three_btn = Button(root,text=3,padx=40, pady=20, command=lambda: button_click(3)).grid(row=4, column=2)
four_btn = Button(root, text=4,padx=40, pady=20, command=lambda: button_click(4)).grid(row=3,column=0)
five_btn = Button(root, text=5,padx=40, pady=20, command=lambda: button_click(5)).grid(row=3,column=1)
six_btn = Button(root, text=6,padx=40, pady=20, command=lambda: button_click(6)).grid(row=3,column=2)
seven_btn = Button(root, text=7,padx=40, pady=20,command=lambda: button_click(7)).grid(row=2, column=0)
eight_btn = Button(root, text=8,padx=40, pady=20, command=lambda: button_click(8)).grid(row=2,column=1)
nine_btn = Button(root, text=9,padx=40, pady=20, command=lambda: button_click(9)).grid(row=2,column=2)
minus_btn = Button(root, text='-',padx=40, pady=20, command= button_minus).grid(row=2,column=3)
add_btn = Button(root, text='+',padx=40, pady=20, command= button_add).grid(row=3, column=3)
divide_btn = Button(root, text='/',padx=40, pady=20,command= button_divide).grid(row=4,column=3)
multiply_btn = Button(root, text='x',padx=40, pady=20, command= button_multiply).grid(row=5,column=3)
clear_btn = Button(root,text='clear',padx=80, pady=20, command= button_clear ).grid(row=5, column=1, columnspan=2)
equal_btn = Button(root, text='=',padx=120,pady=20, command= button_equal).grid(row=6,column=0,columnspan=4)









root.mainloop()