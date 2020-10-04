import collections
t = 10,20,30
print(isinstance(t,collections.Hashable))
print(hash(t))

d ={}
t =(10,20,30)

d[t]='a'

print(d)


t = eval(input('enter tuple of no:'))
print('the sum :',sum(t))
print('the avarage:',sum(t)/len(t))
