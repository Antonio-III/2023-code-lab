from tkinter import *
import re
from tkinter import messagebox
main = Tk()
main.title("Validating user names")
main.geometry("300x450")
main['bg']='#22263d'


def validate_username():
    
    valid_names=r'^[A-Za-z][A-Za-z0-9]{6,11}$'
    username  = Name_Entry.get()
    # Validate username here using Regular expression
    if re.match(valid_names,username):
        messagebox.showinfo('Success','Valid name')
    else:
        messagebox.showerror('Failed','Invalid name')
        



    
#create a label
heading = Label(main, text="Enter user name with alphanumeric characters \n 1. Starts with alphabet. \n 2. Minumim 7 characters and maximum 12 ", 
                font=('Roboto', 10),fg="#FFFFFF" ,bg="#22263d")
heading.place(x=20,y=10)

#Create text area to read contents from the file
Name_Entry = Entry(main)
Name_Entry.place(x=20, y=100,height=25, width=250)

#Create a button to open the file
Button(
    main, 
    text="Validate", 
    command=validate_username
    ).place(x=20, y=200, height=25, width=250)

main.mainloop()
