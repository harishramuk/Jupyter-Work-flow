class stud:
    def __init__ (self,name,age,mark,rno):
        self.name = name
        self.age = age
        self.mark = mark
        self.rno = rno

    def __str__(self):
        
        return('\t\n name :{}\n\t age:{}\n\t mark:{}\n\t rno:{}'
              .format(self.name,self.age,self.mark,self.rno))
        
s = stud('harris',28,500,77)
print(s)