#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
    def carinfo(self):
        print('\tCar-name ={}\n\tCar-model ={}\n\tCar-color ={} '.format(self.name,self.model,self.color))
        
class Persion:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def address(self):
        print('Address:Hosaroad,Bangalore')
class Employee(Persion):
    def __init__ (self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno = eno
        self.esal= esal
        self.car = car
    def work(self):
        print('python Developer...')
        
    def eminfo(self):
        print('Employee name:',self.name)
        print('Employee age:',self.age)
        print('Employee eno:',self.eno)
        print('Employee esal:',self.esal)
        print('Employee information...')
        self.car.carinfo()
        
c = Car('Innova','v2','Black')
e = Employee('Harris',28,777,20000,c)
e.address()
e.work()
e.eminfo()