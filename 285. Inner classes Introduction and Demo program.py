class outer:
    def __init__(self):
        print('outer class object...')
        
    class inner:
        def __init__(self):
            print('inner class object...')
            
        def m1 (self):
            print('m1 object creation')
            
outer().inner().m1()
