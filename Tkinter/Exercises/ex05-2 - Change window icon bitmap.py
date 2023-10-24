import tkinter as tk

# Create an output window
main = tk.Tk()

# Create a base window size
main.geometry('600x600')

# Change default title
main.title('Change icon using iconbitmap')

# Create a text at the top
# Grid default is 0,0. Previous grid row/columns must be made before making a new one, else will display at the lowest uncreated grid 
tk.Label(main,text='Top text').grid()

# ---CHANGE THE ICON USING ICONBITMAP---
main.iconbitmap('Images/favicon.ico')

# ----------

# Start the app
main.mainloop()
