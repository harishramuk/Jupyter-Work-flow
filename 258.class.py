class student:
    def __init__(self,Name,Rno,Mark):
        self.name = Name
        self.rno = Rno
        self.mark = Mark

    def take (self):
        print('Name:',self.name)
        print('R.No:',self.rno)
        print('Mark:',self.mark)



s=student(Name= input('enter the stu name:'),
          Mark=int(input('enter the no:')),
          Rno=int(input('enter the Roll-no:'))
          )
s.take()
