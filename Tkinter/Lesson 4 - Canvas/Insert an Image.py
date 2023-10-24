import tkinter as tk
from PIL import ImageTk, Image

# Create an output window
main = tk.Tk()

# Set a base window size
main.geometry('600x600')

# Set a title
main.title('Insert an Image to Canvas')


# ---CREATE A CANVAS---
canvas = tk.Canvas(main, width=400, height=400, bg='white')

# Output the canvas
canvas.pack()


# ---OPEN AND LOAD THE IMAGE---

# Can use 'Image.Open() or just 'file='
image = ImageTk.PhotoImage(file='Images/BSULOGO.png')

# ---OUTPUT THE IMAGE------
canvas.create_image(200,60,image=image)



# Start the App
main.mainloop()
