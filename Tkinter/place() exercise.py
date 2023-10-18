from tkinter import *

main = Tk()

main.title("Find & Replace but with place()")

main.geometry('600x600')


# Vars

entry_width = 280

# We have a custom height because I want the 'Entry' to have the approx. same height as the 'Button'
entry_height = 25



column_1 = 50 # x coord

# We add a 1 to not cause an overlap between 2 elements
button_x = (column_1 + entry_width)+1

button_width = 80



# ----------


# Row 0
# ----------

# Content

# 'Find:' Text
# place(): We need to pass at least 1 argument  
Label(main,text='Find:').place(x=0)

# Input line
# place: We can pass 'width'
Entry(main).place(x = column_1, width = entry_width, height = entry_height)


#'Find' button
# We place it +1 higher than its width to create a small gap
Button(main, text='Find').place(x=button_x, width=button_width)

# ----------



# Row 1 (y = 20)

# Vars

row_1 = 20 # y coord

# The 'Button' class is taller than 'Entry' or 'Label', we add this to subsequent rows so they don't look misaligned
offset = 8 # y coord

row_1_y = row_1+offset
# ----------


# 'Replace' Text
Label(main,text='Replace:').place(y=row_1_y)

# Input line
Entry(main).place(x=column_1,y=row_1_y,height =entry_height,width=entry_width)

# 'Find All' button
Button(main,text='Find All').place(x=button_x,y=row_1_y, width = button_width)


# ----------

# Row 2 (y = 60)

# Vars

row_2 = 60 # y coord
column_2 = 220 # x coord
# ----------

#Align the 'label' with the 'checkbutton''s text
label_offset = 2

#Align the button
button_offset = 4

# ----------

# Checkbutton
Checkbutton(main,text='Match whole word only').place(x=column_1,y=row_2)

# 'Direction' Text
Label(main, text = 'Direction:').place(x=column_2,y = row_2+label_offset)

# 'Replace' button
Button(main,text = 'Replace').place(x = button_x, y= row_2-button_offset, width= button_width)


# ----------

# Row 3 (y = 80)

# Vars

# y coord
row_3 = 80

# x coords
column_3 = column_2 + 50 
column_4 = column_3 + 50

# Create a small space between the row 3's checkbutton and row 2's
checkbutton_offset = 5

#Align the buttons' text with the checkbuttons'
radiobutton_offset = 5

button_offset = 5
#----------

#Checkbutton
Checkbutton(main,text='Match Case').place(x =column_1,y = row_3+checkbutton_offset)

# 2 Radiobuttons
Radiobutton(main,text='Up').place(x=column_2, y =row_3+radiobutton_offset)

Radiobutton(main,text='Down').place(x=column_3,y=row_3+radiobutton_offset)

# 'Replace All' Button
Button(main,text='Replace All').place(x = button_x,y = row_3+button_offset,width = button_width)

# ----------



# Row 4 (y = 120)

# Vars
row_4 = 110
# ----------
Checkbutton(main,text = 'Wrap Around').place(x = column_1,y = row_4)
# Start App
main.mainloop()
