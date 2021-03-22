f = open('abc.txt','w')
print('file name:',f.name)
print('file mode:',f.mode)
print('file close:',f.closed)
print('is file readable:',f.readable())
print('is file readable:',f.writable())

f.close()

print('is file close :',f.closed)