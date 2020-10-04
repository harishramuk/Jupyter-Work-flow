l = [1,2,3,4,5]
print('before list:',l)
re = int(input('enter the removing element:'))
if re in l:
    l.remove(re)
    print('after removing l:',l)
else:
    print(re,'element not avalable')    
    
    