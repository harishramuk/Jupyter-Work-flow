class test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def inva(self):
        print('insid access variable:',self.a)
t = test()
t.inva()
print('out side access variable:',t.b)        


class test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    def inva(self):
        del self.a
t = test()
print(t.__dict__) 

t1 = test()
t1.inva()
del t1.c
print('t1 object print:',t1.__dict__)

t2 = test()
del t2.a,t2.b
print('t2 object will print:',t2.__dict__)