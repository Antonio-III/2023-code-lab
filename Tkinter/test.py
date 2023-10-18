# Import the GUI (tkinter)
from tkinter import * # '*' means all

# Create an output window
root = Tk()

# Rename the GUI's title
root.title('Find & Replace')

# Resize the default dimensions W,H
root.geometry('600x600')


class MyButton(Button):
    def grid(self,row,column,sticky,padx):
        row = self.row
        column = self.column
        sticky = self.sticky
        padx = 6










# Row 0

# The Label widget is just plain text
Label(root,
      text = 'n').grid(sticky=E) # row/column is 0 by default. We count by cross axis


# Entry widget is an input line

# 'columnspan' takes space of NON-EMPTY cells starting from above its default value (1). Having more 'columnspan' than non-empty cells will have no immediate effect (you have to fill columns to show effect)
# We have to declare 'row' otherwise it will add itself on the bottom-right of the last element
# We declare a 'sticky' because by default, the widget will not fill the cells given, so we 'sticky' it to 'WestEast' to expand fully in its cell. This is because other 'button' cells have different content sizes, so to match them all, we apply 'sticky=we'
Entry(root).grid(row=0,column=1,columnspan=3,sticky='we')

MyButton(root, text = 'n').grid(row = 0, column =4,sticky='we')





# Row 1

Label(root,
      text= 'Replace:').grid(row=1)


Entry(root).grid(row=1,column=1, columnspan=3,sticky='we')


Button(root,
       text = 'Find All').grid(row=1,column=4,sticky='we')

# Row 2

Checkbutton(root,text='Match whole word only').grid(row=2, column=1)


Label(root, text = 'Direction:').grid(row=2, column=2)

Button(root,text='Replace').grid(row=2, column =4,sticky='we')

# Row 3

# We 'sticky' the second button because the longest 'checkbutton' dictates the width of the cell
Checkbutton(root,text='Match Case').grid(row=3,column=1, sticky='w')

# We need a value of 'n' and 'n+1'. To press be able to press 1 button at a time. Last button will be checked no matter what.
# Radiobutton can only be checked 1 at a time
Radiobutton(root, text = 'Up',value =0).grid(row=3, column=2)
Radiobutton(root, text = 'Down',value=1).grid(row=3, column=3)


Button(root, text='Replace All').grid(row=3, column=4,stick='we')


# Row 4
Checkbutton(root, text= 'Wrap Around').grid(row=4,column=1, sticky='w')
root.mainloop()


# Outside


