import tkinter as tk

root=tk.Tk()
font=('Tahoma',16)
root.geometry('400x400')
root['bg']= 'lightgoldenrod1'

def output():
    with open('text files/203.txt') as file:
        contents=file.readlines()
        contents_string=''
        for i in contents:
            contents_string+=i
        
        t.delete('1.0','end')
        print(contents)
        print(f'String: {contents_string}')
        t.insert(tk.END,contents_string)
        t.insert(tk.END,f'\nLen of string: {len(contents_string)}')
        t.insert(tk.END,f'\nCounts newline character as 1 char')
        
t=tk.Text(root,font=font)
t.place(relx=.5,relwidth=.8,relheight=.5,anchor='n')
# (root,from_,to,bg,fg,font,text,command)
b=tk.Button(root,bg='cornflowerblue',fg='lightgoldenrod1',font=font,text='Open and Read file',command=output)
b.place(relx=.5,rely=.6,anchor='c')
