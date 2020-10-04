s = 'ADAABBCCDA'
output=''
for ch in s:
    if ch not in output:
        output=output+ch
print (''.join(sorted(output))) 


s ='AABBDDEECC' 
l =[]
for ch in s:
    if ch not in l:
        l.append(ch)
print (''.join(sorted(l))) 


s = 'AACCDDBB' 
s1 =set(s)

print (''.join(sorted(s1)))
  