from beverage import Beverage
from abc import abstractmethod

class Condinment(Beverage):
    
    @abstractmethod
    def getdescription(self):
        pass
