import tkinter as tk

# Create an output window
root = tk.Tk()

# Set a base window size
root.geometry('600x600')


# ---CREATE A CANVAS---

# arguments : (output window, width, height, bg color)
canvas = tk.Canvas(root, width= 400, height = 400, bg ='black')

# Display the object using a 'geometry'. We put in a separate line for clarity
canvas.pack()


# ---IN THE CANVAS, DRAW LINES---

# Draw a rectangle

# X axis
# For a horizontal line, the Y value will stay the same for 1 line

# y = 10 for line 1
canvas.create_line(10,10,390,10,fill='white',width=2, dash =(1,1))

# y = 110 for line 2 
canvas.create_line(10,110,390,110,fill='white',width=2)


# Y axis

# Y-Line 1 will connect X-Line 1 and 2's start point. Y-L 2 will connect X-L 1 and 2's endpoint
canvas.create_line(10,10,10,110,fill='white',width=2)

canvas.create_line(390,10,390,110,fill='white',width=2)



# ---CREATE A RECTANGLE---

# Rectangle
canvas.create_rectangle(10,200,390,300,fill='red', width=1)

# -----------


# Start the app
root.mainloop()
