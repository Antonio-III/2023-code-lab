from tkinter import *

main = Tk()

main.title("Find & Replace but with place()")

main.geometry('600x600')

# Vars

# Generate 5 variables with the values : 0, 30, 60, 90, 120
row = [30*i for i in range(5)]

# ----------

# Create 5 variables wih the values: 0, 50, 250, 300
column = []
increment = 0

for i in range(4):
    if i == 2:
        column.append(250)
        increment = 250
    else:
        column.append(increment)

    if i >2:
        increment+=100
    else:
        increment+=50

# ----------


entry_width = 350 # Takes away x coords.


# We have a custom height because I want the 'Entry' to be approx. the same height as the 'Button'. Chose divisible by 5
entry_height = 25

# Consistent width across all buttons
button_width = 80

# We add a 1 to not cause an overlap between 2 elements ('Entry' and 'Button')
column.append(column[1] + entry_width + 1)

# ----------



# Row 0

# 'Find:' Text
Label(main,text='Find:').place(x=0) # place(): We need to pass at least 1 argument  

# Input line
Entry(main).place(x = column[1], width = entry_width, height = entry_height) # place: We can pass 'width'


#'Find' button
Button(main, text='Find').place(x=column[4], width=button_width) 

# ----------



# Row 1 

# 'Replace' Text
Label(main,text='Replace:').place(y=row[1])

# Input line
Entry(main).place(x=column[1],y=row[1],height=entry_height,width=entry_width)

# 'Find All' button
Button(main,text='Find All').place(x=column[4],y=row[1], width = button_width)


# ----------



# Row 2

#Align the 'Label' with the 'Checkbutton''s text
label_offset = 2 # y coord

# ----------

# Checkbutton
Checkbutton(main,text='Match whole word only').place(x=column[1],y=row[2])

# 'Direction' Text
Label(main, text = 'Direction:').place(x=column[2],y = row[2]+label_offset)

# 'Replace' button
Button(main,text = 'Replace').place(x = column[4], y= row[2], width= button_width)


# ----------



# Row 3 

#Checkbutton
Checkbutton(main,text='Match Case').place(x =column[1],y = row[3])

# 2 Radiobuttons
Radiobutton(main,text='Up').place(x=column[2], y =row[3])

Radiobutton(main,text='Down').place(x=column[3],y=row[3])

# 'Replace All' Button
Button(main,text='Replace All').place(x =column[4],y = row[3],width = button_width)

# ----------



# Row 4

Checkbutton(main,text = 'Wrap Around').place(x = column[1],y = row[4])

# ----------



# Start App
main.mainloop()
