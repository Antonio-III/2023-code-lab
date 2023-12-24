import tkinter as tk
class Animal():
    def __init__(self,name,age,type_):
        self.name=name
        self.age=age
        self.type=type_

    def animaldetails(self):
        details=f'Name: {self.name}\nAge: {self.age}\nType: {self.type}'
        return details


animal=[Animal('peter',21,'dog'),Animal('jo',10,'cat'),Animal('L',15,'lion')]
for i in animal:
    print(f'{i.animaldetails()}\n')

# ---

class AnimalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Animal Information App')
        self.geometry('400x400')
        self['bg']='black'
        
    
if __name__=='__main__':
    AnimalApp().mainloop()
