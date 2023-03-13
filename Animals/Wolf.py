from Animal import Animal


class Wolf(Animal):

    def __init__(self, world, position, age, newBorn, madeAction, strength=9):
        super().__init__(world, strength, 5, position, age, newBorn, madeAction)

    def draw(self):
        print("W")

    def createSameOrganism(self, coordinates):
        return Wolf(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "Wolf"
        return name

    def color(self):
        return "yellow"