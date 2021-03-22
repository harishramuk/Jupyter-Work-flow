fname = input('enter the file name:')
f = open(fname,'w')
while True:
    data = input('enter the data:')
    f.write(data+'\n')
    option = input('do ypu want to add some more data[yes/no]')
    if option.lower()=='no':
        break
f.close()
print('your providing data written...')