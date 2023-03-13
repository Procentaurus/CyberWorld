import random
from Animal import Animal
from Point import Point


class Fox(Animal):

    def __init__(self, world, position, age, newBorn, madeAction, strength=3):
        super().__init__(world, strength, 7, position, age, newBorn, madeAction)

    def draw(self):
        print("F")

    def createSameOrganism(self, coordinates):
        return Fox(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "Fox"
        return name

    def color(self):
        return "orange"

    def canItRun(self, attackingOrganism):
        if attackingOrganism.getStrength() > self._strength:
            x = random.randint(0, 1)
            if x == 1:
                return True
            else:
                return False
        return False

    def checkField(self, position):
        if self._world.doesFieldExist(position):
            if self._world.isFieldOccupied(position):
                table = self._world.getOrganismsTable()
                if table[position.x][position.y].getStrength() <= self._strength:
                    return True
                else:
                    return False
            else:
                return True
        return False

    def fieldForFoxToMove(self):
        fields = [-1] * 8
        x = self._position.x
        y = self._position.y

        point = Point(x - 1, y - 1)
        if self.checkField(point):
            fields[0] = 1
        point.changeNumbers(x, y - 1)
        if self.checkField(point):
            fields[1] = 1
        point.changeNumbers(x + 1, y - 1)
        if self.checkField(point):
            fields[2] = 1
        point.changeNumbers(x + 1, y)
        if self.checkField(point):
            fields[3] = 1
        point.changeNumbers(x + 1, y + 1)
        if self.checkField(point):
            fields[4] = 1
        point.changeNumbers(x, y + 1)
        if self.checkField(point):
            fields[5] = 1
        point.changeNumbers(x - 1, y + 1)
        if self.checkField(point):
            fields[6] = 1
        point.changeNumbers(x - 1, y)
        if self.checkField(point):
            fields[7] = 1

        return fields

    def action(self):
        whereCanFoxGo = self.fieldForFoxToMove()
        newPosition = self.findPlaceForNewOrganism(whereCanFoxGo)
        indexOfMove = self.tranformIntoMoveIndex(newPosition)
        super().actionWithIndex(indexOfMove)

