
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.e_no = eno
        self.e_name = ename
        self.e_sal = esal
        self.e_addr = eaddr
        
    def display1(self):
        print('E-NO:{}\nE-NAME:{}\nE-SAL:{}\nE-ADDR:{}\n'
              .format(self.e_no,self.e_name,self.e_sal,self.e_addr))