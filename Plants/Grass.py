from Plant import Plant


class Grass(Plant):
    def __init__(self, world, position, age, newBorn, madeAction):
        super().__init__(world, 0, position, age, newBorn, madeAction)

    def draw(self):
        print("g")

    def createSameOrganism(self, coordinates):
        return Grass(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "Grass"
        return name

    def color(self):
        return "green"
