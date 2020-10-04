class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def display(self):
        print('hai',self.name)
        print('your mark is:',self.mark)
    def avg (self):
        if self.mark >= 60:
            print('your got a first class...')
        elif self.mark >= 50:
            print('your got a second class...')
        elif self.mark >= 35:
            print('your got a third class...')
        else:
            print('your faile...')
        
        
n = int(input('enter the number of student:'))
for x in range (n):
    name = input('enter the student name:')
    mark = int(input('enter the student mark:'))
    s=student(name,mark)
    s.display()
    s.avg()
    print()