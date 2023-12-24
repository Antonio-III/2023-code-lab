# 165 of the ppt 

import tkinter
from tkinter import messagebox
from PIL import ImageTk,Image
from random import randint

# all the code below will not execute unless this function is called.
def app():
    # create an output window
    main = tkinter.Tk()

    # window size
    main.geometry('600x600')

    # title
    main.title('Exercise on 165 ppt')
    #---
    def font(**kwargs):
        size=kwargs.get('size',16)
        
        font_style=['Tahoma',size]
        
        if 'bold' in kwargs:
            font_style.append('bold')
        
        return tuple(font_style)           
    #---

    #Develop a GUI to perform followung task
    # 1. Create two button. First button as "Show info", second as "Yes or no"
    # 2. When user clicks "Show info" button, display the showinfo message box using event handler
    # 3. When user clicks "Yes or no" button display the askyesno message box, based on the value selected, perform the following:
        # a. if yes is selected, display "You selected Yes" as a label
        # b. display "You selected No" if otherwise

    def showinfo():
        messages=['You took the red pill','You are now red-pilled']
        
        index=randint(0,len(messages)-1)
        
        messagebox.showinfo('Successful','You clicked button 1')
        
        l2.configure(text=messages[index])
        
    def askyesno():
        
        messages=['You took the blue pill','You are now blue-pilled']
        
        response=messagebox.askyesno('Question','Continue?')
        
        index=randint(0,len(messages)-1)
        
        if response:
            l2.configure(text=messages[index])
        else:
            l2.configure(text='Canceled the blue pill')

    # app 
    bg_imgo = Image.open('Images/Red_and_blue_pill.jpg')
    bg_imgr= bg_imgo.resize((600,600))

    bg_img= ImageTk.PhotoImage(bg_imgr)

    picture_label = tkinter.Label(main,image=bg_img).place(x=0)
    l1=tkinter.Label(main,text='To be or not to be?')
    l1.place(relx=.5,rely=.1,anchor='n')

    b1=tkinter.Button(main,text='To Be',command=showinfo,bg='#e93e29',)
    b1.place(relx=.16,rely=.43,relwidth=.2)

    b2=tkinter.Button(main,text='Not To Be',command=askyesno,bg='#4062c5')
    b2.place(relx=.62,rely=.43,relwidth=.2)

    b_list=[b1,b2]
    for i in b_list:
        i.configure(fg='white',font=font())

    l2=tkinter.Label(main,font=font(),text='Which pill do you take?')
    l2.place(relx=.5,rely=.8,anchor='center')

    l_list=[l1,l2]

    for i in l_list:
        i.configure(bg='#9d9d9d',fg='white',font=font(size=20,bold=1))

    # start the app
    main.mainloop()


    
# call the function
app()
