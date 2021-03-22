

#COMPOSITION -- IS- A Relationship Demo program

class persion:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def address(self):
        print('HOSA ROAD,BANGALORE')
class employee(persion):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal
    def work(self):
        print('python devloper...')
    def empinfo(self):
        print('employe name:',self.name)
        print('employe age:',self.age)
        print('employe eno:',self.eno)
        print('employe esal:',self.esal)
e = employee('harris',9741516890,777,20000)
e.address()
e.work()
e.empinfo()


