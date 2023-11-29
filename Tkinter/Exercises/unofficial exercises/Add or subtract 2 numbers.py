import tkinter as tk


# root window
main=tk.Tk()

# window size
main.geometry('600x600')

# set title
main.title('Add and Subtract numbers')          


# app (row, top to bottom)
font=('Tahoma',15)


label1=tk.Label(main,text='Enter first number: ',font=font)
label1.place(relx=0)          

entry1=tk.Entry(main)
entry1.place(relx=.35,height=25)

label2=tk.Label(main,text='Enter second number: ',font=font)
label2.place(rely=.1)

entry2=tk.Entry(main)
entry2.place(relx=.35,rely=.1,height=25)

button1=tk.Button(main,text='ADD',font=font,command=lambda: label4.configure(text=int(entry1.get()) + int(entry2.get()))) 
button1.place(relx=.5,rely=.2,anchor='e',width=125)

button2=tk.Button(main,text='SUBTRACT',font=font,command=lambda: label4.configure(text=int(entry1.get()) - int(entry2.get())))
button2.place(relx=.5,rely=.2,anchor='w',width=125)

label3=tk.Label(main,text='Output',font=font)
label3.place(relx=.5,rely=.3,anchor='c')

label4=tk.Label(main,font=font)
label4.place(relx=.5,rely=.35,anchor='c')


# start the app
main.mainloop()          
