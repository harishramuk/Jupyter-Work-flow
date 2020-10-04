l = [1,2,1,2,3,4]
x = int(input('enter the element find to index:'))
if x in l:
    print('{} present in index :{}'.format(x,l.index(x)))
else:
    print(x,'is not avalable in list')    