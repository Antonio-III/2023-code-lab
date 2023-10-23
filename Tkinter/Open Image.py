from tkinter import *
from PIL import ImageTk, Image


# Create an output window
root=Tk()

# Create a base window size
root.geometry('600x600')

# Insert an image to and store in a var
img=ImageTk.PhotoImage(Image.open('Images\marek-szturc-8Ou3EZmTMWA-unsplash.jpg'))

Label(root, image = img)
Label.pack()

# Start the app
root.mainloop()
