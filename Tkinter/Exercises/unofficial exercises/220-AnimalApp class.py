import tkinter as tk

class AnimalApp(tk.Tk):
    
    class Animal:
        def __init__(self,**kwargs):
            self.name=kwargs.get('name')
            self.age=kwargs.get('age')
        def stats(self):
            return f'Name: {self.name} \nAge: {self.age}'
        
    def display(self):
        self.text_one.delete('1.0',tk.END)
        
        for element in self.animals_inst:
            animal_details= element.stats()
            self.text_one.insert(tk.END,animal_details+'\n\n')
            
    def __init__(self):
        super().__init__()
        self.title('Animal App')
        self.geometry('500x500')
        
        self['bg']='lightgoldenrod1'
        self.font=('Tahoma',12)
        self.w_preset={'font':('Tahoma',12),'bg':'lightgoldenrod1','fg':'cornflowerblue'}
        
        self.animals_inst=[self.Animal(name='Yasuo',age=12),self.Animal(name='Yone',age=14),self.Animal(name='Kayn',age=16)]

        self.button_one=tk.Button(self,**self.w_preset,text='Display Animal Details',command=self.display)
        self.button_one.place(relx=.5,anchor='n')

        self.text_one=tk.Text(self,font=self.font)
        self.text_one.place(relx=.5,rely=.5,anchor='c',relwidth=.5,relheight=.5)


if __name__=='__main__':
    AnimalApp().mainloop()
