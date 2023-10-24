# Import the required momdules
from tkinter import *
from PIL import ImageTk, Image

# Create an output window
root = Tk()

# Set a base window size
root.geometry('600x600')

# Set a title 
root.title('Working with image icons')

# ---CHANGE THE ICON---

# Top text
Label(root, text= 'Change window icon').pack()

# If 1st argument is 'True' the icon will apply to all windows. If not, only main will apply
root.iconphoto(False,ImageTk.PhotoImage(Image.open('Images/favicon.ico')))

# Start the app
root.mainloop()