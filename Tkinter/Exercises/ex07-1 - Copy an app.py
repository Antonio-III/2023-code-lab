# Import tkinter and represent it as 'tk'
import tkinter as tk

#import 2 PIL functions or whatever
from PIL import ImageTk, Image

# ---SETUP THE APP---

# Create an output window
root = tk.Tk()

# Set title
root.title('Copy a design')

# Set a base window size
root.geometry('350x600')

# Make app unresizable: takes 2 int args
root.resizable(0,0)

root['bg'] = 'white'


# ---(1) CHANGE THE ICON WINDOW---
root.iconbitmap('Images/logo1.ico')


# ---(2) INSERT AN IMAGE---
banner_img = ImageTk.PhotoImage(file='Images/BSULOGO.png')

picture_1 = tk.Label(root, image = banner_img)

# Output the image
picture_1.place(x=0) #.place() takes at least 1 arg


# ---(3) CREATE A FRAME---

white_frame = tk.Frame(root,bg='white')

# .grid() does not accept 'width', so we use .place()
white_frame.place(rely=.2, width =350,height=150)


# ---(3.5) CREATE A LABEL AND USE FRAME AS CONTAINER---

# Put a label using the frame as a container (text not displayed yet)
sms = tk.Label(white_frame,text= 'Student \nManagement\n System',font=('Roboto',25),bg = 'white', fg ='#22263d')

# Output the label
sms.place(relx=.5,rely=.5, anchor = 'center') # When in doubt, use 'anchor'


# ---(4) CREATE ANOTHER FRAME---
image_frame = tk.Frame(root,bg='red')

# Output the image
image_frame.place(rely=.45,width=350,height=400)


# ---(5) INSERT ANOTHER IMAGE---

# We will resize the image
img = Image.open('Images/image2.png')

# Update the var with the resized image
img = img.resize((350,500))

# Update the var once again by loading the image
img = ImageTk.PhotoImage(img)

# Attach the image to a widget
picture_2 = tk.Label(image_frame, image = img)

# Output the image
picture_2.place(x=0)


# ---(6) CREATE A BUTTON WIDGET---
tk.Button(image_frame, # Button is to be placed using 'image_frame' as the container'
       text='Click Here',
       width = 20,
       height = 2,
       bg='#22263d',
       fg = 'white',
       font = ('Roboto', 12)). place(relx=.5,rely = .7, anchor ='center')

# Start the app
root.mainloop()
