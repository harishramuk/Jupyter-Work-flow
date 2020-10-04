def wish(name,meg):
    print('hello',name,meg)
wish('harish','good mor')


def wish(name = 'durga',meg = 'good mor'):
    print('hello',name,meg)
wish()
wish('harris')
wish('harish' ,'good even')


def wish(name,meg='good mor'):
    print('hello',name,meg)
wish('harish')


# this is fault
def wish(name='durga',meg):
    print('hello',name,meg)
wish(name='harish',meg='good mor')
    