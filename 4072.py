
import jsonpickle

class Employee:
    def __init__(self,eno,ename,esal,eaddr,ismarried):
        self.eno = eno
        self.ename = ename
        self.esal= esal
        self.eaddr = eaddr
        self.ismarried = ismarried
    def display(self):
        print('E-NO:{},E-NAME:{},E-SAL:{},E-ADDR:{}'.format(self.eno,self.ename,
                                                            self.esal,self.eaddr))
e = Employee( 7,'harris',60000,'chennai',True)

json_str = jsonpickle.encode(e)
print(json_str)

with open('empobject407.json','w') as f:
    f.write(json_str)
    
with open('empobject407.json','r') as f:
    
    jsonstr = f.readline()
    
    e2 = jsonpickle.decode(jsonstr)
e2.display()