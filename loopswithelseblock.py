card=[10,20,30,40,50,60]
for item in card:
    if item >=500:
        print('you connot  place this order..',item)
        break
    
    print('processing item :',item)
else:
    print('congratulation all items processed suessfuly..')
    
    
    
print('item>500')

card=[10,20,30,40,505,600]
for item in card:
    if item >=500:
        print('you connot  place this order..',item)
        break
    
    print('processing item :',item)
else:
    print('congratulation all items processed suessfuly..')  
    
    
    
    print('continue')
    
card=[10,20,30,40,505,606]
for item in card:
    if item >=500:
        print('you connot  place this order..',item)
        continue 
    
    print('processing item :',item)
else:
    print('congratulation all items processed suessfuly..')    