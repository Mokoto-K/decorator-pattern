from abc import ABC, abstractmethod

class Beverage(ABC):

    def __init__(self) -> None:
        self.description = "Unknown beverage"


    def getdescription(self):
        return self.description
    

    @abstractmethod
    def cost(self):
        pass
