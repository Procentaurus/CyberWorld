from Plant import Plant


class WolfBerry(Plant):
    def __init__(self, world, position, age, newBorn, madeAction):
        super().__init__(world, 99, position, age, newBorn, madeAction)

    def draw(self):
        print("B")

    def createSameOrganism(self, coordinates):
        return WolfBerry(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "WolfBerry"
        return name

    def isFightingDeadly(self):
        return True

    def color(self):
        return "darkGray"

