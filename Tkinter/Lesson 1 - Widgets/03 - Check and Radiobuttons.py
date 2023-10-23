# Import the GUI module
from tkinter import * #from library import * (all)


#create an output window
root = Tk()

root.title('First App') # Rename the application's title (tk by default)

root.geometry('600x600') # Creates an output with dimensions W * H

root.resizable(0,0) # Makes the output window's size unchangable. Only if it's (0,0)

Label(root,
      text = "Antonio Miguel",
      #fg = "black",
      #bg = "white",
      font = ("Arial", 30)).grid() #default grid is 0,0


# We 'sticky' subsequent widgets because the first creates the row size, and we want our items to be aligned in 1 direction
Label(root, 
       text = "Course: CC",
       #fg = "yellow",
       #bg = "black",
       font = ("Arial", 20)).grid(row=1,sticky='w')


Label(root, 
       text = "Group 3",
       #fg = "white",
       #bg = "black",
       font = ("Arial", 20)).grid(row=1,column=1,sticky='w')


Label(root,
      text='My hobbies:',
      font = ("Arial", 20)).grid(row=2,sticky='w')

Checkbutton(root,
            text='League of Legends',
            font = ("Arial", 15)).grid(row=3,sticky='w')

Checkbutton(root,
            text='League of Legends',
            font = ("Arial", 15)).grid(row=3,column=1,sticky='w')

Checkbutton(root,
            text='League of Legends',
            font = ("Arial", 15)).grid(row=4,sticky='w')

Checkbutton(root,
            text='Walking',
            font = ("Arial", 15)).grid(row=4,column=1,sticky='w')

Label(root,
      text='Future Career:',
      font = ("Arial", 20)).grid(row=5,sticky='w')

Radiobutton(root,
            text='Software Engineer',
            font=('Arial',15),
            value=0).grid(row=6,sticky='w')

Radiobutton(root,
            text='Web Developer',
            font=('Arial',15),
            value=1).grid(row=6,column = 1,sticky='w')

Radiobutton(root,
            text='Fullstack Dev',
            font=('Arial',15),
            value=2).grid(row=7,sticky='w')


# mainloop() indicates your application is ready to run and it tells the code to keep displaying 
# ALL CODE MUST BE WRITTEN BEFORE .mainloop()!!
root.mainloop()
