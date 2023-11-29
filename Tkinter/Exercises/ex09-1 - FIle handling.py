import tkinter as tk

def myfunc():
    t1.delete('1.0','end')
    with open('Text files/notepad.txt') as file:
        file_string=""
        for i in file.readlines():
            file_string+=i

        # for gui    
        t1.insert(tk.END,f'{file_string}\n')
        t1.insert(tk.END,f'Length of "file_string": {len(file_string)}')

        # for console
        print(f'{file_string}')
        print(f'Length of "file_string": {len(file_string)}')
        
# set root window
root= tk.Tk()

# title
root.title('Reading text file')

# base window size
root.geometry('600x600')

t1=tk.Text(root)
t1.place(relx=.5,anchor='n',relheight=.5,relwidth=1)
        
tk.Button(root,text='Open File',bg='black',fg='white',command=myfunc).place(relx=.5,rely=.5,anchor='n')
# start the app
root.mainloop()
