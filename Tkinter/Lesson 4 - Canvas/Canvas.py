from tkinter import *

# Create an output window
root = Tk()

root.geometry('600x600')

# arguments : (output window, width, height, bg color)
canvas = Canvas(root, width= 400, height = 400, bg ='black')

# Display the object using a 'geometry'. We put in a separate line for clarity
canvas.pack()


# Draw a rectangle

# X axis
# For a horizontal line, the Y value will stay the same

# y = 10 for line 1
canvas.create_line(10,10,390,10,fill='white',width=2, dash =(1,1))

# y = 110 for line 2 
canvas.create_line(10,110,390,110,fill='white',width=2)


# Y axis
# Copy and paste the 2 line's startpoints/endpoint as your own startpoint and endpoint
canvas.create_line(10,10,10,110,fill='white',width=2)

canvas.create_line(390,10,390,110,fill='white',width=2)

# Rectangle
canvas.create_rectangle(10,200,390,300,fill='red', width=1)


# Start the app
root.mainloop()
