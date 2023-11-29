import tkinter as tk

def key_press(event):
    l2.configure(text=event.char)
    
root=tk.Tk()

root.geometry('400x400')
root.title('174 of the ppt')

#app
f1=tk.Frame(root,bg='red')
f1.place(relwidth=1,relheight=1)


l1=tk.Label(f1,bg='blue',fg='white',font=('Tahoma',20,'bold'),text='The key you pressed is:')
l1.place(relx=.5,relwidth=1,relheight=.2,anchor='n')

l2=tk.Label(f1,bg='red',fg='white',font=('Tahoma',20,'bold'))
l2.place(relx=.5,rely=.3,anchor='c')

# <Key> only works on root window, it seems
root.bind('<Key>',key_press)
root.mainloop()
