try:
    x = int(input('enter the namber:'))
    y = int(input('enter the number :'))
    print('result :', x/y)
except BaseException as meg:
    print('exception type:',type(meg))
    print('exception type:',meg.__class__)
    print('exception name:',meg.__class__.__name__)
    print('discription..:',meg)