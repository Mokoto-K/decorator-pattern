from beverage import Beverage

class Espresso(Beverage):

    def __init__(self) -> None:
        super().__init__()
        self.description = "Espresso"

    def cost(self):
        return 1.99
