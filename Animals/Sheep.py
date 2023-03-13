from Animal import Animal


class Sheep(Animal):

    def __init__(self, world, position, age, newBorn, madeAction, strength=4):
        super().__init__(world, strength, 4, position, age, newBorn, madeAction)

    def draw(self):
        print("S")

    def createSameOrganism(self, coordinates):
        return Sheep(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "Sheep"
        return name

    def color(self):
        return "black"
