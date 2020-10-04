d = {100:'a',300:'b',200:'c'}
k = int(input('enter the key :'))

if k in d:
    print('the coresponding value:',d[k])
    print('the coresponding value:',d.get(k))
else:
    print(k,'the specified key is not applicable')    