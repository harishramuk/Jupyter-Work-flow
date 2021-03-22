from zipfile import *
f = ZipFile('GSP.zip','r',ZIP_STORED)
names = f.namelist()
print('file name:',names)
for name in names:
    f1 = open(name,'r')
    text = f1.read()
    print('name of files:',name)
    print(text)
    f1.close()
    print()
        
    
    
        