import tkinter as tk

root=tk.Tk()
font=('Tahoma',16)

def display_file():
    # first, delete contents of text widget
    text_widget.delete('1.0','end')
    # then, open the file
    with open('Text Files/195.txt') as file_handler:
        content=file_handler.read()
    # insert content into text widget
    text_widget.insert(tk.END,content)
    
root.title('add scrollbar')
root.geometry('500x500')
root['bg']='lightgoldenrod1'

text_widget=tk.Text(root,font=font)
text_widget.place(relx=.5,relwidth=.8,relheight=.4,anchor='n')

# add scrollbar widget
scrollbar_widget=tk.Scrollbar(root,orient='vertical')
scrollbar_widget.place(relx=.9,relheight=.4)

# so the scrollbar works properly when the user drags and holds the widget
scrollbar_widget.config(command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar_widget.set)

# (root,from_,to,bg,fg,font,text,command)
button_widget=tk.Button(root,bg='cornflowerblue',fg='black',font=font,text='Open File and Read',command=display_file)
button_widget.place(relx=.5,rely=.5,anchor='c')
