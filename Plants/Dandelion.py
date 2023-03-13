from Plant import Plant


class Dandelion(Plant):
    def __init__(self, world, position, age, newBorn, madeAction):
        super().__init__(world, 0, position, age, newBorn, madeAction)

    def draw(self):
        print("D")

    def createSameOrganism(self, coordinates):
        return Dandelion(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "Dandelion"
        return name

    def action(self):
        for i in range(3):
            super().action()
        self._age -= 2

    def color(self):
        return "cyan"
