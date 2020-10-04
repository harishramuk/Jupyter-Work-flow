t = (10,20,30,40)
r = reversed(t)
t1 =tuple (r)
print(t1)


t = (10,15,5,25,20)
r = sorted(t)
t1 =tuple (r)
print(t1)


t = (10,15,5,25,20)
r = sorted(t,reverse=True)
t1 =tuple (r)
print(t1)

a =10
b = 20
c = 30
d = 40
t =a,b,c,d
print(t)

t =(10,20,30,40)
a,b,c,d = t
print(a,b,c,d)

t =(10,20,30,40)
a,b,c,d= t
print(a,b,c,d)

t = (x*x for x in range(1,6))
print(type(t))
print(tuple (t))