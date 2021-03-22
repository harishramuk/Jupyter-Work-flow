f = None
try:
    f = open('login.txt','r')
except:
    print('some problems while locating and opening the file..')
    
else:
    print('file is open successfully..')
    print('the data present in the file is:')
    print(f.read())
finally:
    if f is not None:
        f.close()