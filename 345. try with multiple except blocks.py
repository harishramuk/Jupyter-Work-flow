try:
    x = int(input('enter the namber:'))
    y = int(input('enter the number :'))
    print('result :', x/y)
except ZeroDivisionError:
    print('cannot divide with zero...')
except ValueError:
    print('plese provied int value...')
   
