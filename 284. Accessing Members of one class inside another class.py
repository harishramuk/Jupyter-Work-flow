class employ:
    def __init__(self,name,eno,esal):
        self.employee_name = name
        self.employee_no = eno
        self.employee_sal = esal
    def display(self):
        print('Employe name:',self.employee_name)
        print('Employe Rollno:',self.employee_no)
        print('Employe salary:',self.employee_sal)
class manager:
    def updateempsal(emp):
        emp.employee_sal = emp.employee_sal + 10000
        emp.display()
emp = employ('Harris',7,40000)
manager.updateempsal(emp)

