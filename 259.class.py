class test:
    def __init__(self):
        print('this is self:',id(self))
t = test()
print(id(t))
