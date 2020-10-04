class test:
    a = 10
    def __init__(self):
        test.b = 20
    def mi (self):
        test.c = 30
    @classmethod
    def mi1(cls):
        cls.d = 40
        test.e = 50
    @staticmethod
    def mi2():
        test.f = 60
        
        
t = test()
t.mi()
t.mi1()
t.mi2()
test.g=70
print(test.__dict__)
        