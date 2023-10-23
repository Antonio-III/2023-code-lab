from tkinter import *
from PIL import ImageTk, Image


# Create an output window
root=Tk()

# Create a base window size
root.geometry('600x600')

# Insert an image to and store in a var
img=ImageTk.PhotoImage(Image.open('Images/polar-bear-484515_640.jpg'))

picture = Label(root, image = img)

# Output the picture
picture.pack()

# Start the app
root.mainloop()
