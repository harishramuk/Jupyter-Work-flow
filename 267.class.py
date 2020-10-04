


class test:
    def __init__(hack):
        hack.a = 10
        hack.b = 20
    def inst (punk):
        punk.c = 30
t = test()
t.inst()
t.d= 40

t1 = test()
t1.inst()
t1.e = 50
print(t.__dict__) 
print(t1.__dict__) 
       
        