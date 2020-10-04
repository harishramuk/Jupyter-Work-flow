def f1(**a):
    print(a)
f1()
f1(name='harris',roll_no = 100)
f1(a=100,b=200)


def f1(*a,b = 10):
    print(a)
    print(b)
f1(10,20,30,b=40)    
