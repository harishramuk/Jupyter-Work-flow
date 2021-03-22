class persion:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        
    def display (self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('City:',self.city)
class employee(persion):
    def __init__(self, name, age, city,eno,esal):
        super().__init__(name, age, city)
        self.eno = eno
        self.esal = esal
    def display(self):
        super().display()
        print('Eno:',self.eno)
        print('Esal:',self.esal)
        
e = employee('harris',28,'Bangalore',777,50000)
e.display()