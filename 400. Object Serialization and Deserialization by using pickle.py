import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.e_no = eno
        self.e_name = ename
        self.e_sal = esal
        self.e_addr = eaddr
        
    def display1(self):
        print('E-NO:{},E-NAME:{},E-SAL:{},E-ADDR:{}'.format(self.e_no,
                                                            self.e_name,
                                                            self.e_sal,
                                                            self.e_addr))
        
E = Employee(7,'harris',50000,'chennai')

with open('EMP.txt','wb') as f:
    pickle.dump(E,f)
    print('pickling of employe object completed...')
    
with open('EMP.txt','rb') as f:
    newob=pickle.load(f)
    print('unpickling of emp obj is completed...')
    
    newob.display1()