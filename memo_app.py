from tkinter import *
import time

db = ['python', 'java', 'c++', 'html']

root = Tk()
root.title('MEMO')


'''e = Entry(root, width=75,borderwidth=10)
e.grid(row=1,column=0,columnspan=8)
e.insert(0, 'type your memo here:')'''


title = "Welcome to the memo app"
title_2 = Label(root, text=title)
title_2.grid(row=0, column=0)


def add_memo():
    global e
    e = Entry(root, width=75,borderwidth=10)
    e.grid(row=8,column=0,columnspan=8)
    e.insert(0, 'type your memo here:')
    global memo
    memo = 'add'

def edit_memo():
    global memo
    memo = 'edit'
    global e
    e = Entry(root, width=75,borderwidth=10)
    e.grid(row=8,column=0,columnspan=8)
    out_2 = Label(root,text='Select the number of the memo you wish to edit:')
    out_2.grid(row=9,column=0)
    out_2.after(10000, out_2.destroy)
    out_3 = Label(root, text=db)
    out_3.grid(row=10,column=0)
    out_3.after(50000, out_3.destroy)

def delete_memo():
    global memo
    memo = 'delete'
    global e
    e = Entry(root, width=75,borderwidth=10)
    e.grid(row=8,column=0,columnspan=8)
    out_2 = Label(root,text='Select the number of the memo you wish to delete:')
    out_2.grid(row=9,column=0)
    out_2.after(10000, out_2.destroy)
    out_3 = Label(root, text=db)
    out_3.grid(row=10,column=0)
    out_3.after(50000, out_3.destroy)

def read_memo():
    global memo
    memo = 'read'
    out = Label(root, text=db)
    out.grid(row=11,column=0)
    out.after(50000, out.destroy)

def exit_memo():
    root.quit()
    
    
    
def submit():
    if memo == 'add':
        e.after(1000,e.destroy)
        db.append(e.get())
        out = Label(root, text="Memo added succesfully")
        out.grid(row=len(db)+11,column=0)
        out.after(2000, out.destroy)
    if memo == 'edit':
        user_input = e.get()
        e_2 = Entry(root, width=75,borderwidth=10)
        e_2.insert(0, f'Type what you want to be replaced with')
        e_2.grid(row=len(db)+10,column=0,columnspan=8)
        def edit_2():
            e_2.after(1000,e_2.destroy)
            e.after(1000, e.destroy)
            db[int(user_input)-1] = e_2.get()
            out_2 = Label(root, text='Memo edited sucessfully')
            out_2.grid(row=15,column=0)
            out_2.after(2000, out_2.destroy)
        edit2_btn = Button(root, text='Edit',command=edit_2).grid(row=len(db)+10,column=9)
        
    if memo == 'delete':
        user_input = e.get()
        e.after(1000, e.destroy)
        db.pop(int(user_input)-1)
        out_2 = Label(root, text='Memo deleted successfully')
        out_2.grid(row=15,column=0)
        out_2.after(2000, out_2.destroy)
        print(db)
       

        




add_btn = Button(root, text='ADD MEMO', padx=30, pady=10,command=add_memo).grid(row=3, column=0) 
edit_btn = Button(root, text='EDIT MEMO', padx=30, pady=10, command=edit_memo).grid(row=4,column=0)
delete_btn = Button(root, text='DELETE MEMO', padx=30, pady=10,command=delete_memo).grid(row=5,column=0)
read_btn = Button(root, text='READ MEMO', padx=30, pady=10,command=read_memo).grid(row=6,column=0)
quit_btn = Button(root, text='EXIT MEMO', padx=30, pady=10, command=exit_memo).grid(row=7,column=0)
submit_btn = Button(root,text="SUBMIT",command=submit).grid(row=3,column=8)







root.mainloop()