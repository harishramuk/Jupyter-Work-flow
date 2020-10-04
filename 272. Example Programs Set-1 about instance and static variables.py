class test:
    a = 10
    def __init__(self):
        test.a = 20
    def mi (self):
        test.a = 30
    @classmethod
    def mi1(cls):
        cls.a = 40
        test.a = 50
    @staticmethod
    def mi2():
        test.a = 60
        
        
t = test()
t.mi()
t.mi1()
t.mi2()
test.a=70
print(test.a)