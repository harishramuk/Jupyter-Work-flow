
l=[1,1,1,12,2,2,3,3,3]
print('before removing list',l)
re = int(input('enter remove element:'))
while True:
    if re in l:
        l.remove(re)
    else:
        break
print(l)    
    