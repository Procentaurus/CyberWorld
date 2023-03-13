import random

from Animal import Animal


class Antelope(Animal):

    def __init__(self, world, position, age, newBorn, madeAction, strength=4):
        super().__init__(world, strength, 4, position, age, newBorn, madeAction)

    def draw(self):
        print("A")

    def createSameOrganism(self, coordinates):
        return Antelope(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "Antelope"
        return name

    def color(self):
        return "red"

    def canItRun(self, attackingOrganism):
        if attackingOrganism.getStrength() > self._strength:
            x = random.randint(0, 1)
            if x == 1:
                return True
            else:
                return False
        return False

    def action(self):
        position = self.getPosition()
        super().action()
        if self not in self._world.getToRemove():
            super().action()
            self._age -= 1
