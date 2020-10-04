def f1(a,*b):
    print(a)
    for x in b:
        print(x)
    print(b)
f1(10,20,30,40)


def f1(*a,b):
    print(*a)
    print(b)
f1(70,50,60,b=100)

def f1(*a):
    print(a)
f1(10)    
    
