# datetime library - display current date and time
# webbrowser library - used to open the requested page using default browser
import tkinter as tk
from datetime import *
root=tk.Tk()
font=('Tahoma',16)
root.title('display current date')
root.geometry('500x500')

c_date=datetime.now()
print(c_date)

# %A full name of day
# %B full name of month
# %d full number of day
# %Y full number of year
label=tk.Label(root,font=font,text=f'{c_date:%A, %B, %d, %Y}',bg='yellow')
label.place(y=0)

label1=tk.Label(root,font=font,text=f'{c_date:%d %B %Y}',bg='red')
label1.place(rely=.1)
root.mainloop()
