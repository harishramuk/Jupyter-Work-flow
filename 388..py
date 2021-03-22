import os
fname = input('enter file name:')
if os.path.isfile(fname):
    print('file existing:',fname)
    f = open(fname,'r')
    text = f.read()
    print(40 * '*')
    print(text)
    print(40 * '*')
    f.close()
else:
    print('file name is not exist...')    