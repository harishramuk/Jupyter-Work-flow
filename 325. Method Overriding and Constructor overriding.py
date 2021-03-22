class parent:
    def __init__(self):
        print('parent class')
        
class child(parent):
    def __init__(self):
        super().__init__()
        print('child class ')
        
        
c = child()
