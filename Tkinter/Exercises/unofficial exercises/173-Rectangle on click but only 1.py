import tkinter as tk

rectangle_count=[]
def rectangle(mousepos):
    
    x,y=mousepos.x,mousepos.y

    rectangle=canvas.create_rectangle(x,y,x+60,y+40,fill='yellow',outline='black')
    rectangle_count.append(rectangle)

    if len(rectangle_count) > 1:
        canvas.delete(rectangle_count[-2])
       
    print(len(rectangle_count))
# root iwndow
root=tk.Tk()

root.title('173 of the ppt')
root.geometry('500x500')

# app 
canvas=tk.Canvas(root,bg='red')
canvas.place(relheight=1,relwidth=1)

canvas.bind('<Button-1>',rectangle)


# start app
root.mainloop()
