import tkinter as tk
import re
from tkinter import messagebox
root=tk.Tk()


e1_string=tk.StringVar()
e2_string=tk.StringVar()
font=('Tahoma',16)

def switch_frames():
    l3_text=e1_string.get()
    l4_text=e2_string.get()
    switch=True
    if len(l3_text)==0 and len(l4_text)==0:
        l3.configure(text=f'You forgot your name, bruh!')
        l4.configure(text=f'And your age, too!')

    else:
        if len(l3_text)>0:
            valid_name=r'^[A-Z][A-Z]*[a-z]*$'
            if re.match(valid_name,l3_text):
                l3.configure(text=f'Good morning, {l3_text}!')
            else:
                messagebox.showerror('Error','Invalid name. Must start with Uppercase.')
                switch=False
        else:
            l3.configure(text=f'You forgot your name, bruh!')
        if len(l4_text)>0:
            # REGEX that requires to start and end with 1 or more digits. Effectively creating a match if it only contains numbers.
            valid_pw=r'^\d+$'
            if re.match(valid_pw,l4_text):
                if re.match(r'^[1]$',l4_text):
                    l4.configure(text=f'You are {l4_text} year old? You lie.')
                elif re.match(r'^[0234567]$',l4_text):
                    l4.configure(text=f'You are {l4_text} years old? You lie.')
                else:   
                    l4.configure(text=f'You are aged: {l4_text}. Is that right?')
                
            else:
                messagebox.showerror('Error','Invalid age. Must only contain numbers.')
                switch=False
        else:
            l4.configure(text=f'You forgot your age, {l3_text}!')
            
    if switch==True:
        frames[-1].tkraise()
        frames[0],frames[1]=frames[-1],frames[0]
 
            
root.title('179 of the ppt')
root.geometry('400x400')

f1=tk.Frame(root,bg='green')
f1.place(relheight=1,relwidth=1)

f2=tk.Frame(root,bg='blue')
f2.place(relheight=1,relwidth=1)

# in f1 (row, left to right)
l1=tk.Label(f1,text='Enter name:',bg='green',font=font)
l1.place(x=0)

e1=tk.Entry(f1,font=font,textvariable=e1_string)
e1.place(relx=.3)

l2=tk.Label(f1,text='Enter age:',bg='green',font=font)
l2.place(rely=.1)

e2=tk.Entry(f1,font=font,textvariable=e2_string)
e2.place(relx=.3,rely=.1)

b1=tk.Button(f1,text='Switch frames',command=switch_frames,font=font)
b1.place(relx=.5,rely=.3,anchor='c')

# in f2
l3=tk.Label(f2,bg='blue',font=font)
l3.place(relx=.5,anchor='n')

l4=tk.Label(f2,bg='blue',font=font)
l4.place(relx=.5,rely=.1,anchor='n')


b1=tk.Button(f2,text='Switch frames',command=switch_frames,font=font)
b1.place(relx=.5,rely=.3,anchor='c')

frames=[f1,f2]
f1.tkraise()
root.mainloop()
