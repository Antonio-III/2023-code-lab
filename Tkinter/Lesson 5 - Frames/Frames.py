import tkinter as tk

def app():
    font=('Tahoma',16)
    colors=['crimson','aqua']
    
    f_ppreset={'relwidth':.5,'relheight':1}
    l_ppreset={'relx':.5,'rely':.4,'anchor':'c'}

    
    leftframe = tk.Frame(root,bg=colors[0])
    leftframe.place(**f_ppreset)
    
    rightframe=tk.Frame(root,bg=colors[1])
    rightframe.place(relx=.5,**f_ppreset)

    frames=[leftframe,rightframe]

    text=['Red','Blue']

    for i in frames:
        tk.Label(i,font=font,bg=colors[frames.index(i)],text=f'{text[frames.index(i)]} Frame').place(**l_ppreset)

    
# Create an output window
root = tk.Tk()
# Set a title
root.title('Frames')
# Set a base window size
root.geometry('600x600')
# call function
app()
# Start the app
root.mainloop()

