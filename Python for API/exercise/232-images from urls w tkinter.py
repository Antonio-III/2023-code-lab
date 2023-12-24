import tkinter as tk
from PIL import ImageTk,Image
import requests,io

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Juice Wrld')
        self.geometry('350x600')
        
        self.font=('Tahoma',16)
        self.bg=self.resize(1,'Images/bg.png',350,600)

        self.background=tk.Label(self,image=self.bg)
        self.background.place(relwidth=1)

        self.top_text=tk.Label(self,bg='black',font=self.font,fg=self.convert_rgb((232,160,0)),text='Juice Wrld')
        self.top_text.place(relx=.5,rely=.15,anchor='n')

        self.drink_image=tk.Label(self)
        
        self.drink_text=tk.Label(self)
        
        self.button=tk.Button(self,bg=self.convert_rgb((232,160,0)),fg='black',font=self.font,text='Get Drink',command=self.random_drink)
        self.button.place(relx=.5,rely=.8,anchor='s')
    
    def resize(self,mode,directory,width,height):
        if mode==1:
            b_img= Image.open(directory)
        elif mode==2:
            b_img=Image.open(io.BytesIO(directory))

        r_img=b_img.resize((width,height))
        img=ImageTk.PhotoImage(r_img)
        return img
    
    def convert_rgb(self,tuple_val):
        return '#%02x%02x%02x' % tuple_val

    def random_drink(self):
        url='https://www.thecocktaildb.com/api/json/v1/1/random.php'
        url_get=requests.get(url)
        print(url_get)
        if url_get.__str__()=='<Response [200]>':
            self.url_json=url_get.json()

            self.drink_img()
            self.drink_txt()
            
    def drink_img(self):
        image_url=self.url_json['drinks'][0]['strDrinkThumb']
        image_get=requests.get(image_url)

        if image_get.__str__()=='<Response [200]>':
            self.drink_image.destroy()
            
            self.image=self.resize(2,image_get.content,200,200)

            self.drink_image=tk.Label(self,image=self.image)
            self.drink_image.place(relx=.5,rely=.4,anchor='c')
            
    def drink_txt(self):
        self.drink_text.destroy()

        self.drink_name=self.url_json['drinks'][0]['strDrink']
        
        self.drink_text=tk.Label(self,bg='black',fg=self.convert_rgb((232,160,0)),font=self.font,text=self.drink_name)
        self.drink_text.place(relx=.5,rely=.65,anchor='s')
                
if __name__=='__main__':
    App().mainloop()
