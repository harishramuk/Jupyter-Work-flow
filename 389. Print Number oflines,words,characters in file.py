import os

fname = input('enter the file name:')
if os.path.isfile(fname):
    print('file is exist',fname)
    f = open(fname,'r')
    lcount = ccount = wcount= 0
    
    for lin in f:
        lcount = lcount + 1
        ccount = ccount + len(lin)
        words_of_cur_line = line.split()
        wcount = wcount+ len(words_of_cur_line)
    print('No of line :',lcount)
    print('no of chr:',ccount)
    print('No of words:',wcount)
    
else:
    print('this file is not exist:',fname)