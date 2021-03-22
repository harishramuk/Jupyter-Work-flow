try:
    x = int(input('enter the first value:'))
    y = int(input('enter the sec value:'))
    print('result:',x/y)
    
except (ZeroDivisionError,ValueError) as msg:
    print('the raised exception:', msg.__class__.__name__)
    print('discription of exception:',msg)
    print('pls provied valied input...')
    