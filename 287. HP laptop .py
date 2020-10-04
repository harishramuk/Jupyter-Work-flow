class Laptop:
    def __init__(self,name):
        print('laptop object is creating...')
        self.name = name
        self.process = self.Process()
       # Laptop.process = Laptop.Process()   
       
    def info (self):
        print('This laptop Brand is',self.name)
        print('Good Running Modal..')
        self.process.model()
        self.process.os.version()
    
    class Process:
        def __init__(self):
            print('Processes object creating...')
            #Laptop.Process.os = Laptop.Process.Os()
            self.os = self.Os()
        def model (self):
            print('model is i7 with 16-Gb ram.. ')
        class Os:
            def __init__(self):
                print('windos OS object creating...')
            def version (self):
                print('Windos 10 Updated version is avaliable.. ')
                
laptop = Laptop('HP')
laptop.info()