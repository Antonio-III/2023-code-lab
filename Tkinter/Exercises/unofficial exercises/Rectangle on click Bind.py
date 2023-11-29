import tkinter as tk

def rectangle(mouse):
    x,y=mouse.x, mouse.y

    canvas.create_rectangle(x,y,x+60,y+40,fill='black',outline='yellow')

# root window
root = tk.Tk()

root.title('Rectangle on click')

root.geometry('500x500')

canvas=tk.Canvas(root,bg='red',width=500,height=500)
canvas.place(relx=0)

canvas.bind("<Button-1>", rectangle)


# start app
root.mainloop()
