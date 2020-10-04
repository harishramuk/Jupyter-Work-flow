class student:
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    def setmark(self,mark):
        self.mark = mark
    def getmark(self):
        return self.mark 
    
n = int(input('enter the number of student: '))
students=[]
for x in range(n):
    s=student()
    Name = input('enter the name:')
    Mark = int(input('enter the mark:'))
    s.setname(Name)
    s.setmark(Mark)
    students.append(s)
    
for s in students:
    print('hi',s.getname())
    print('your mark is:',s.getmark())
    print()