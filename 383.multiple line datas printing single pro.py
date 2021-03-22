file = open('mobno.txt','r')
line = file.readline()
print(line)
while line != '':
    print(line,end='')
    line = file.readline()
file.close()