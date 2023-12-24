import tkinter as tk

root=tk.Tk()
font=('Tahoma',16)
def display_file():
    # first, delete contents of text widget
    # '1.0' is read as a row/column. row 1, column 0 (first character)
    # 'end' means it goes from '1.0' to 'end' of the text, why it's string idk
    text_widget.delete('1.0','end')
    
    # then, open the file
    with open('Text Files/195.txt') as file_handler:
        content=file_handler.read()
        
    # insert content into text widget
    # tk.END is like 'end' ie end of the text, which is the start because it all got deleted.
    # 'content' is the text to insert
    text_widget.insert(tk.END,content)
    
root.title('But contents of file on widget')
root.geometry('500x500')
root['bg']='lightgoldenrod1'
text_widget=tk.Text(root,font=font)
text_widget.place(relx=.5,relwidth=.8,relheight=.4,anchor='n')

# (root,from_,to,bg,fg,font,text,command)
button_widget=tk.Button(root,bg='cornflowerblue',fg='black',font=font,text='Open File and Read',command=display_file)
button_widget.place(relx=.5,rely=.5,anchor='c')
