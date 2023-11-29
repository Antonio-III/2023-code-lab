import tkinter

# Create an output window
root=tkinter.Tk()

# Set a title
root.title('Display name')

# Set a window size
root.geometry('600x600')



# ------FUNCTIONS AND VARS---------

bg_color = '#234567'

user_name=tkinter.StringVar()

font_style = ('Arial',15)

text = 'Your name is: '

def onClick():
    name = user_name.get()
    name_is.configure(text=f'{text} {name}')

#--------------------------

root['bg']=bg_color

#------------------

# Label
name=tkinter.Label(root,text='Enter Name',bg=bg_color,fg='white',font=font_style)
name.place(relx=.05,rely=.05)

# Entry
tkinter.Entry(root,textvariable=user_name,font=font_style).place(relx=.3,rely=0.05)

# Button
show_name = tkinter.Button(root,text='Show name',command=onClick,font=font_style, bg='yellow',fg='#001111')
show_name.place(relx=0.35, rely=0.15)

# Label
name_is=tkinter.Label(root,text=text,bg=bg_color,fg='white',font=font_style)
name_is.place(relx=.05,rely=.25)


#--------------------

# Start the app
root.mainloop()
