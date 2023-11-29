class Cat():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Cat name: {self.name}")



cat1=Cat("catname",21)

cat2=Cat("earn",42)
cat2.display()


class Dog():
    def __init__(self,name,age,color,weight):
        self.name=name
        self.age=age
        self.color=color
        self.weight=weight
    def display(self):
        message=f'Dog stats: \nName: {self.name}, Age: {self.age}, Color: {self.color}, Weight: {self.weight}'
        print(message)
    


dog1=Dog('Brownie',21,'black','50kg')
dog1.display()

dog2=Dog('China',3,'orange','3kg')
dog2.display()
