f = open('abc.txt','w')
f.write('ALL STUDENTS ARE STUPIDS')
with open('abc.txt','r+') as f:
    text = f.read()
    print('data before modificatio...')
    print(text)
    
    print('the current cursor position:',f.tell())
    f.seek(17)
    f.write('GEMS!!!')
    f.seek(0)
    text=f.read()
    print('data after modification...')
    print(text)