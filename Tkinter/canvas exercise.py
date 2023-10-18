from tkinter import *
# INCOMPLETE CODE


# Create an output window
root = Tk()

# Set base size
root.geometry('600x600')


canvas = Canvas(root,width=400,height=400,bg='black')
canvas.pack()

# Draw a house

# Roof
# arguments: start coords, end coords, color, width
# Line 1 coords
line1_start = (10,10)
canvas.create_line(10,10, 390,10,fill='lightblue',width=2)
canvas.create_line(10,
# Start the app
root.mainloop()
