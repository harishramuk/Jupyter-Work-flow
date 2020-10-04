class outer:
    def __init__(self):
        print('outer object creation...')

    class inner:
        def __init__(self):
            print('inner object creation..')
            
        class innerinner:
            def __init__(self):
                print('innerinner object creation...')
            @staticmethod    
            def m1 ():
                print('m1 object will creating...')
                
outer().inner().innerinner().m1()
    
            