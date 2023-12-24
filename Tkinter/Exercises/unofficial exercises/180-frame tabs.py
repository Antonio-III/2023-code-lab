import tkinter as tk

root=tk.Tk()
font=('Tahoma',16)
tabppreset={'rely':.1,'relwidth':1,'relheight':1}
labelppreset={'relx':.5,'rely':.5,'anchor':'c'}

def switch(target_tab):
    global active_widgets

    for i in active_widgets:
        i.destroy()
        
    
    bg=['yellow','red','aqua','chartreuse1']
    fg=['black','yellow','crimson','violetred']
    
    frame=tk.Frame(root,bg=bg[target_tab])
    frame.place(**tabppreset)

    text=tk.Label(frame,bg=bg[target_tab],fg=fg[target_tab],font=font,text=f'This is tab {target_tab+1}!')
    text.place(**labelppreset)
    
    active_widgets=[frame,text]
    
root.geometry('500x500')

# (root,from_,to,bg,fg,font,text,command)
tabs=tk.Frame(root,bg='grey')
tabs.place(relwidth=1,relheight=.1)

tab1=tk.Button(tabs,font=font,text='Tab 1',command= lambda: switch(0))
tab1.place(relwidth=.25,relheight=1)

tab2=tk.Button(tabs,font=font,text='Tab 2',command= lambda: switch(1))
tab2.place(relx=.25,relwidth=.25,relheight=1)

tab3=tk.Button(tabs,font=font,text='Tab 3',command= lambda: switch(2))
tab3.place(relx=.5,relwidth=.25,relheight=1)

tab4=tk.Button(tabs,font=font,text='Tab 4',command= lambda: switch(3))
tab4.place(relx=.75,relwidth=.25,relheight=1)

# On-start tab
start_tab=tk.Frame(root,bg='black')
start_tab.place(**tabppreset)

text_s=tk.Label(start_tab,bg='black',fg='white',font=font,text='Press a tab to switch frames!')
text_s.place(**labelppreset)
#---

active_widgets=[start_tab,text_s]

root.mainloop()
