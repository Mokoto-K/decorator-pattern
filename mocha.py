from condiment import Condinment
import beverage

class Mocha(Condinment):
    def __init__(self, beverage) -> None:
        self.beverage = beverage


    def getdescription(self):
        return f"{self.beverage.getdescription()}, Mocha"


    def cost(self):
        return self.beverage.cost() + 0.20
