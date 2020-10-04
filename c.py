class test:
    def __init__(self,name,rno,mark):
        print('constructor exciqut...')
        self.name=name
        self.rno = rno
        self.mark = mark
t = test('harris',101,200)
t.__init__()



