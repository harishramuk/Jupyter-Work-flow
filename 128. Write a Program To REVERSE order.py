s = 'durga soft solution'
l=s.split()
l1=l[::-1]
output = ' '.join(l1)
print(output)


a = s.split()
a1=[]
for word in a:
    a1.append(word[::-1])
output =' '.join(a1) 
print(output)   