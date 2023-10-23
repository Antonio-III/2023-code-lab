from tkinter import *
from PIL import ImageTk, Image

# Create an output window
root = Tk()

# Set base window size
root.geometry('600x600')

# Set a bg color
root['bg'] = 'green'

# Set a title
root.title('Resizing an Image')

# Set a text on top of the image
Label(root, text='Top text').pack()


# --- RESIZING AN IMAGE ---

# Load the image by using 'Image.open'
base_img = Image.open('Images/polar-bear-484515_640.jpg')

# Apply the resize by passing a tuple that corresponds to W,H
resize_img = base_img.resize((200,200))

# Open the image using 'PhotoImage'
ready_resize_img = ImageTk.PhotoImage(resize_img) 

# Attach the image to a widget 'Label'
display_resize_img = Label(root,image = ready_resize_img)

display_resize_img.pack()

# --- 

# Set a text on bottom of the image
Label(root, text='Bottom text').pack()

# ---

# Start the app
root.mainloop()
