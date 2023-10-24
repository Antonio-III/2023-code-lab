import tkinter 
# INCOMPLETE CODE


# Create an output window
root = tkinter.Tk()

# Set base window size
root.geometry('600x600')

# Create canvas

max_width = max_height = 400
canvas = tkinter.Canvas(root,width=max_width,height=max_height,bg='black')

# Output the canvas
canvas.pack()

# ---DRAW A HOUSE---

# ROOF

# arguments: start coords, end coords, color, width

center = (200,10)
x_center, y_center = center

roof_line_height = 150

# Line 1 coords
line1_start = (x_center, y_center)
line1_end = (5,roof_line_height)

canvas.create_line(*line1_start, *line1_end ,fill='lightblue', width=3)


# Line 2 coords
line2_start = (x_center, y_center)
line2_end = ((max_width-line1_end[0]),roof_line_height)

canvas.create_line(*line2_start, *line2_end, fill='lightblue', width=3)

# Line 3
line3_start = line1_end # (5,150)
line3_end = line2_end # (395, 150)
canvas.create_line(*line3_start, *line3_end, fill='lightblue', width=3)


# BODY

# Line 1
# We want: 10px inserted after starting point of line 3. And 5px off the ground = max_height-5 
body_line1_start = (5+10, 150)
body_line1_end = (5+10, max_height-5)

canvas.create_line(*body_line1_start, *body_line1_end, fill='lightgreen', width=3)


# Line 2

# 15 is the X-pos of line 1
body_line2_start = (max_width-15, 150)
body_line2_end = (max_width-15, max_height-5)

canvas.create_line(*body_line2_start, *body_line2_end, fill='lightgreen', width=3)


# Line 3

canvas.create_line(*body_line1_end, *body_line2_end, fill='lightgreen', width =3)

# -----------


# Start the app
root.mainloop()
