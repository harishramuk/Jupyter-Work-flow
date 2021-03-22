from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def noofweel(self):
        pass
class bus(vehicle):
    def noofweel(self):
        return 6
class auto(vehicle):
    def noofweel(self):
        return 3
    
b = bus()
print(b.noofweel())
a = auto()
print(a.noofweel())