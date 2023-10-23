# Import the GUI module
from tkinter import * #from library import * (all)


#create an output window
root = Tk()

root.title('First App') # Rename the application's title (tk by default)

root.geometry('600x600') # Creates an output with dimensions W * H

root.resizable(0,0) # Makes the output window's size unchangable. Only if it's (0,0)

label1 = Label(root,
                text = "Antonio Miguel",
                #fg = "black",
                #bg = "white",
                font = ("Arial", 50)
                ) # Create a label widget to be stored in 'label1'

label1.pack() # Aranges widgets around the edges of the container

label2 = Label(root, 
               text = "Course: CC",
               #fg = "yellow",
               #bg = "black",
               font = ("Arial", 40))
label2.pack(anchor='w')

label3 = Label(root, 
               text = "Group 3     ",
               #fg = "white",
               #bg = "black",
               font = ("Arial", 40))
label3.pack(anchor='w')


# mainloop() indicates your application is ready to run and it tells the code to keep displaying 
# ALL CODE MUST BE WRITTEN BEFORE .mainloop()!!
root.mainloop()
