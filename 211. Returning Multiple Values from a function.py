def sum_sud(a,b ):
    sum = a+b
    sub = a-b
    return sub,sum
print(sum_sud(100,50))


def calc(a,b,c ):
    sum = a+b
    sub = a-b
    mult = a*b
    divd = a//c
    return sub,sum,mult,divd
t=calc(100,50,10)
print(type(t))
print(t)
for i in t:
    print(i)