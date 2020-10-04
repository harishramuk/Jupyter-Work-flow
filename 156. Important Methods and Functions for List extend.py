l1 = [10,20,30]
l2 = [50,60]
l1.append(l2)
print(l1)
print(len(l1))


l1 = [10,20,30]
l2 = [50,60]
l1.extend(l2)
print(l1)
print(len(l1))


l1 = [10,20,30]
l2 = ['abc']
l1.extend(l2)
print(l1)
print(len(l1))


l1 = [10,20,30]

l1.extend('ab12')
print(l1)
print(len(l1))