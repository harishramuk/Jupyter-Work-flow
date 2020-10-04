d ={}
d['a']=100
d['b']=50
print(d.get('a',0)+2)
print(d.get('b',0)+4)
print(d.get('z',0)+2)
print(d)



d ={'a':100,'z':200,'b':400}
for k,v in sorted(d.items()):
    print(k,v)
    
s = 'AACCZBZAADDD'
d ={}
for ch in s:
    d[ch]=d.get(ch,0)+1    
print(d)
for k,v in sorted(d.items()):
    print('{} occurs {} times'.format(k,v))    



s = 'ABAABBCA'
d ={}
output = ''
output1 =''
for ch in s:
    d[ch] = d.get(ch,0)+1
print(d)

for k,v in d.items():
    
    output=output+str(v)+k
    output1=output1+k+str(v)
    
print(output) 
print(output1)   
        
    