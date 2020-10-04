s = 'one two three four five six'
s1=s.split()
i=0
l=[]
while i < len(s1):
    if i%2==0:
        l.append(s1[i])
    else:
        l.append(s1[i][::-1])
    i=i+1
output =' '.join(l)
print(output)





s = 'harish kumar'
i=0
print('even no chr')
while i<len(s):
    print(s[i])
    i=i+2
    
i=1
print('odd no chr')
while i<len(s):
    print(s[i])
    i=i+2    