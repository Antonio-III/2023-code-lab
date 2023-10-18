# Import the GUI module (tkinter)
from tkinter import *

# Create an output window
root = Tk()

root.title('Button App') # Title of the app
 
root.geometry('600x600') # Size of the app



Label(root,
      text = 'Username').grid(row = 0)

Label(root,
      text = 'Password').grid(row = 1)

# We use 'entry' widget. Which is a input box

Entry(root).grid(row=0,
                 column=1)

Entry(root).grid(row=1,
                 column=1)

# 'sticky' Moves items on the (N,E,S,W) of their cell. (if applicable)
# It is applicable here because our button is smaller than the cell (the space taken by 'entry' widgets), so we can move it to West
Button(root, text="Login").grid(row=2,
                                column =1,
                                sticky=E)
# This will run the codes written before this code
root.mainloop()
