class Tooyoungexception(Exception):
    def __init__(self,arg):
        self.meg = arg
        
class Toooldexception(Exception):
    def __init__(self,arg):
        self.meg = arg
        
age = int(input('enter your age:'))
if age > 60:
    raise Toooldexception('''your age is already crossed marriage age no chance of getting marriage''')
elif age < 18:
    raise Tooyoungexception(''' plz wait some more time you will get best match soon''')
else:
    print('you will get match details soon by mail...')