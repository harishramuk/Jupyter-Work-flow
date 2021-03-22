class Persion:
    def __init__(self,name,age,weight,hight):
        self.name = name
        self.age = age
        self.weight = weight
        self.hight = hight
        
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Weight:',self.weight)
        print('Hight:',self.hight)
class Student(Persion):
    def __init__(self,name,age,weight,hight,mark,rno):
        super().__init__(name,age,weight,hight)
        self.mark = mark
        self.rno = rno
    def display(self):
        super().display()
        print('Mark:',self.mark)
        print('R-No:',self.rno)
    def __str__(self):
        return('\t\n name :{}\n\t age:{}\n\t mark:{}\n\t rno:{}'
              .format(self.name,self.age,self.mark,self.rno))
s = Student('Harish',28,50,173,1000,777)
print(s)

s.display()