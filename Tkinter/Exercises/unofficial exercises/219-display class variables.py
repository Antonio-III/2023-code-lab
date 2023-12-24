class run:
    
    class Program:
        def __init__(self):
            self.cat=self.Animal('bob',12,'cat')
            self.dog=self.Animal('sanchez',28,'dog')
            self.cow=self.Animal('rick',42,'cow')

            self.animal_list=[self.cat,self.dog,self.cow]

            for every_element in self.animal_list:
                print(every_element.animalDetails())
                
        class Animal:
            def __init__(self,cname,cage,ctype):
                self.name=cname
                self.age=cage
                self.type=ctype

            def animalDetails(self):
                self.details=f'Name: {self.name}\nAge: {self.age}\nType: {self.type}\n'
                return self.details


if __name__=='__main__':
    run().Program()
