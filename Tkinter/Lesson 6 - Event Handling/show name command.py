import tkinter

# output window
main = tkinter.Tk()

# set title
main.title('display name')

# window size
main.geometry('600x600')


#--Functs and Vars---

preset = {'bg':'#234567',
          'fg':'white',
          'font':('Tahoma',12)
          }

text = f'Your name is:'

user_name=tkinter.StringVar()

def onClick():
        l2.configure(text= f'{text} {user_name.get()}')
              
#--------

main['bg']='#234567'

#-------

# Label
l1 = tkinter.Label(main,text='Enter name',**preset)
l1.place(x=10,y=10)

# Entry
e1 = tkinter.Entry(main,**preset,textvariable=user_name)
e1.place(x=110,y=10)

#Label
l2=tkinter.Label(main,text=text, **preset)
l2.place(x=10,y=100)

#Button
b1=tkinter.Button(main,text='Show name',**preset,command=onClick)
b1.place(x=140,y=50)


#-----


# start the app
main.mainloop()

