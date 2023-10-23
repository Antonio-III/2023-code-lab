from tkinter import *


# Create an output window
root=Tk()

# Create a base window size
root.geometry('600x600')

# Use relative positioning
Label(root, bg = 'red').place(relx=0.5, rely = 0.4)
Label(root, bg = 'blue').place(relx=0.5, rely = 0.5)
Label(root, bg = 'green').place(relx=0.5, rely = 0.6)

# Start the app
root.mainloop()
