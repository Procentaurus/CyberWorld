from Animal import Animal
from Point import Point


class Human(Animal):
    def __init__(self, world, position, age, newBorn, madeAction, strength=5):
        super().__init__(world, strength, 4, position, age, newBorn, madeAction)

    def action(self):
        if not self._madeAction and not self._newBorn:
            indexOfmove = self._world.getHumanIndexMove()
            table = self._world.getOrganismsTable()
            point = Point(0, 0)

            if indexOfmove == 1 and self._world.doesFieldExist(Point(self._position.x, self._position.y - 1)):
                point.changeNumbers(self._position.x, self._position.y - 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x][self._position.y - 1])

            elif indexOfmove == 3 and self._world.doesFieldExist(Point(self._position.x + 1, self._position.y)):
                point.changeNumbers(self._position.x + 1, self._position.y)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x + 1][self._position.y])

            elif indexOfmove == 5 and self._world.doesFieldExist(Point(self._position.x, self._position.y + 1)):
                point.changeNumbers(self._position.x, self._position.y + 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x][self._position.y + 1])

            elif indexOfmove == 7 and self._world.doesFieldExist(Point(self._position.x - 1, self._position.y)):
                point.changeNumbers(self._position.x - 1, self._position.y)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x - 1][self._position.y])

            self._age += 1

    def draw(self):
        print("#")

    def createSameOrganism(self, coordinates):
        return Human(self._world, coordinates, 1, True, True)

    def color(self):
        return "blue"

    def getName(self):
        name = "Human"
        return name

    def isItImmortal(self):
        if self._world.getIsSkillActivated():
            return True
        return False

    def canItRun(self, attackingOrganism):
        if attackingOrganism.getStrength() > self._strength:
            if self._world.getIsSkillActivated():
                return True
            else:
                return False
        else:
            return False
