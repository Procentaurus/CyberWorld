import random

from Animal import Animal


class Tortoise(Animal):

    def __init__(self, world, position, age, newBorn, madeAction, strength=2):
        super().__init__(world, strength, 1, position, age, newBorn, madeAction)

    def draw(self):
        print("T")

    def createSameOrganism(self, coordinates):
        return Tortoise(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "Tortoise"
        return name

    def color(self):
        return "pink"
    def wasAttackBlocked(self, attackingOrganism):
        if attackingOrganism.getStrength() < 5:
            return True
        else:
            return False

    def action(self):
        number = random.randint(0, 99)
        if number > 75:
            super().action()
        else:
            self._age += 1