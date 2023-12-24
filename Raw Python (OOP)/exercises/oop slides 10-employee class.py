class app:
    class Employee:
        def __init__(self,name,salary):
            self.name=name
            self.salary=salary
        def details(self):
            return f'Name: {self.name}, Salary: {self.salary}'
        
    def __init__(self):
        self.employee_1=self.Employee('Bob',1200)
        self.employee_2=self.Employee('Linda',1000)
        
        print(self.employee_1.details())
        print(self.employee_2.details())
            

            

# Instantiate the app class (it will execute its __init__() methodd using the defined constructors, functions, etc.)
app()


