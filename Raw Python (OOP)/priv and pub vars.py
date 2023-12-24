class Cat():
    def __init__(self,name,age):
        self.name=name
        # private var. class-scoped.
        self.__age=age
        self.age=69
    def display(self):
        print(f"Cat name: {self.name}")
    def get_age(self):
        return f"cat's age: {self.age}"




cat1=Cat('Catname',21)

print(cat1.get_age())
print(cat1.name)

# acess a private variable
print(cat1._Cat__age)

print(cat1.age)
