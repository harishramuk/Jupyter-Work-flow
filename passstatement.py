x = int(input('enter marks:'))
if x >=35:
    print('pass mark')
else:
    pass

#adstractmethod
from abc import *
class loan(ABC):
    
    def getintrestRate(self):
        pass
class Homeloan(loan):
    def getintrestRate(self):
        return 8
class Vechicleloan(loan):
    def getintrestRate(self):
        return 11
    
h=Homeloan()
print(h.getintrestRate())
v=Vechicleloan()
print(v.getintrestRate()) 