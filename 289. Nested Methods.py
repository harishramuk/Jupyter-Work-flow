class Test:
    def m1(self):
        i = 1
        while i <=4:
            def cal(a,b):
                print('addition',a+b)
                print('subration',a-b)
                print('multiplication',a*b)
                print('avarage',(a+b)/2)
            i=i+1
            x = int(input('enter the a value:'))
            y = int(input('enter the b value:'))
            cal(x,y)
t=Test()
t.m1()
            