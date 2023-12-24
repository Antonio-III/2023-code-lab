# 171 of the ppt

import tkinter as tk
from random import randint
from tkinter import messagebox
num1=randint(1,10)
num2=randint(11,20)

def sumof(number1,number2):
    answer=number1+number2
    l2.configure(text=answer)
    messagebox.showinfo('Sucessful',f'The sum is {answer}')

    print(number1+number2)
    
# root window
root = tk.Tk()

# window size
root.geometry('400x400')

l1=tk.Label(root,text=f'Your 2 numbers: {num1} and {num2}',font=('Tahoma',18,'bold'))
l1.place(relx=.5,anchor='n')

tk.Button(root,text='Add the numbers',font=('Tahoma',18),command=lambda:sumof(num1,num2)).place(relx=.5,rely=.15,anchor='c')

l2=tk.Label(root,text="",font=('Tahoma',18))
l2.place(relx=.5,rely=.3,anchor='c')
#start app
root.mainloop()

