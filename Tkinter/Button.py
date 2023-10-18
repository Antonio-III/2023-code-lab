# Import the GUI module (tkinter)
from tkinter import *

# Create an output window
root = Tk()

root.title('Button App') # Title of the app
 
root.geometry('600x600') # Size of the app



button1 = Button(root,
                 text = 'Try me!',
                 bg = 'red', # Background (bg) changes the 'button' container
                 width = 20,
                 fg = 'blue') # Foreground (fg) changes the text color
button1.pack()

button2 = Button(root,
                 text = 'Cancel',
                 bg = 'yellow',
                 width=20)
button2.pack()






# This will run the codes written before this code
root.mainloop()
