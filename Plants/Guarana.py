from Plant import Plant


class Guarana(Plant):
    def __init__(self, world, position, age, newBorn, madeAction):
        super().__init__(world, 0, position, age, newBorn, madeAction)

    def draw(self):
        print("G")

    def createSameOrganism(self, coordinates):
        return Guarana(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "Guarana"
        return name

    def canItStrengthen(self):
        return True

    def color(self):
        return "magenta"

