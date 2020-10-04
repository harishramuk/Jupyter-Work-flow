class Engine:
    def __init__(self):
        self.power = '125kw'
        
    def useengine(self):
        print('engine functionality')
        
class car:
    def __init__ (self):
        self.engine = Engine()
    def usecar(self):
        print('car functionality...')
        self.engine.useengine()
        print(self.engine.power)
        
c = car()
c.usecar()