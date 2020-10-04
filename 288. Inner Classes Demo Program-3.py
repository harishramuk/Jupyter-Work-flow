class Persion:
    def __init__(self,name,dd,mm,yyyy):
        print('Persion object is creat...')
        self.name = name
        self.dob = self.Dob(dd,mm,yyyy)
    def info(self):
        print('name:',self.name)
        self.dob.display()
        
    class Dob:
        def __init__(self,dd,mm,yyyy):
            print('Dob object creating...')
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy
        def display (self):
            print('DOB:{}/{}/{}'.format(self.dd,self.mm,self.yyyy))
        
p = Persion('harris',21,2,1991)
p.info()        