import tkinter
from tkinter import messagebox

#create an output window
root = tkinter.Tk()

#set window size
root.geometry('600x600')

#set title
root.title('working with messagebox')

#----------
    
tkinter.Label(root,text='Look at all these buttons!').place(relx=.5,anchor='n')

#---Show message-------
def showInfo():
    #first arg is title of the box, second is its content
    messagebox.showinfo('Title','You pressed the "showinfo" button')

def showError():
    messagebox.showerror('Title','You pressed the "showerror" button!')

def showWarning():
    messagebox.showwarning('Title','You pressed the "showwarning" button!')
    
tkinter.Button(root,text='Click me!',command=showInfo).place(rely=.05)
tkinter.Button(root,text='Click me!',command=showError).place(rely=.1)
tkinter.Button(root,text='Click me!',command=showWarning).place(rely=.15)
                         
#------Ask message---------
def askToCancel():
    messagebox.askokcancel('Question','To Ok or Cancel')

def askRetryCancel():
    messagebox.askretrycancel('Question','To Retry or Cancel')

def askYesNo():
    messagebox.askyesno('Question','Yes or No?')

tkinter.Button(root,text='Click me!',command=askToCancel).place(rely=.05,relx=0.15)
tkinter.Button(root,text='Click me!',command=askRetryCancel).place(rely=.1,relx=0.15)
tkinter.Button(root,text='Click me!',command=askYesNo).place(rely=.15,relx=0.15)

#----------
#start the app
root.mainloop()
