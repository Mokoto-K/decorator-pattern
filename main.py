from espresso import Espresso
from mocha import Mocha

beverage = Espresso()
print(f"{beverage.getdescription()} ${beverage.cost():.2f}")

beverage = Mocha(beverage)
print(f"{beverage.getdescription()} ${beverage.cost():.2f}")


