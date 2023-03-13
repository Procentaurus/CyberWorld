from Animal import Animal
from Plant import Plant
from Point import Point


class Hogweed(Plant):
    def __init__(self, world, coordinates, age, newBorn, madeAction):
        super().__init__(world, 10, coordinates, age, newBorn, madeAction)

    def draw(self):
        print("H")

    def createSameOrganism(self, coordinates):
        return Hogweed(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "Hogweed"
        return name

    def color(self):
        return "gray"

    def lookForAnimalsToKill(self):
        fields = [-1] * 8

        x = self._position.x
        y = self._position.y

        point = Point(x - 1, y - 1)
        if self._world.doesFieldExist(point) and self._world.isFieldOccupied(point):
            fields[0] = 1

        point.changeNumbers(x, y - 1)
        if self._world.doesFieldExist(point) and self._world.isFieldOccupied(point):
            fields[1] = 1

        point.changeNumbers(x + 1, y - 1)
        if self._world.doesFieldExist(point) and self._world.isFieldOccupied(point):
            fields[2] = 1

        point.changeNumbers(x + 1, y)
        if self._world.doesFieldExist(point) and self._world.isFieldOccupied(point):
            fields[3] = 1

        point.changeNumbers(x + 1, y + 1)
        if self._world.doesFieldExist(point) and self._world.isFieldOccupied(point):
            fields[4] = 1

        point.changeNumbers(x, y + 1)
        if self._world.doesFieldExist(point) and self._world.isFieldOccupied(point):
            fields[5] = 1

        point.changeNumbers(x - 1, y + 1)
        if self._world.doesFieldExist(point) and self._world.isFieldOccupied(point):
            fields[6] = 1

        point.changeNumbers(x - 1, y)
        if self._world.doesFieldExist(point) and self._world.isFieldOccupied(point):
            fields[7] = 1

        return fields

    def isFightingDeadly(self):
        return True

    def doesItKillAnimalsAround(self):
        return True

    def huntAnimal(self, x, y):
        table = self._world.getOrganismsTable()
        if isinstance(table[x][y], Animal):
            if table[x][y].isItImmortal():
                print("Human survived attack by Hogweed\n")
            elif table[x][y].doesItHateHogweed():
                print("CyberSheep is close to Hogweed\n")
            else:
                table[x][y].draw()
                print(" in {" + str(table[x][y].getPosition().x) + "," + str(table[x][y].getPosition().y) + "} was killed by Hogweed\n")
                point = Point(x, y)
                list1 = self._world.getToRemove()
                list1.append(table[x][y])
                self._world.deleteElement(point)

    def action(self):
        occupiedFields = self.lookForAnimalsToKill()
        x = self._position.x
        y = self._position.y

        if occupiedFields[0] == 1:
            self.huntAnimal(x - 1, y - 1)
        if occupiedFields[1] == 1:
            self.huntAnimal(x, y - 1)
        if occupiedFields[2] == 1:
            self.huntAnimal(x + 1, y - 1)
        if occupiedFields[3] == 1:
            self.huntAnimal(x + 1, y)
        if occupiedFields[4] == 1:
            self.huntAnimal(x + 1, y + 1)
        if occupiedFields[5] == 1:
            self.huntAnimal(x, y + 1)
        if occupiedFields[6] == 1:
            self.huntAnimal(x - 1, y + 1)
        if occupiedFields[7] == 1:
            self.huntAnimal(x - 1, y)

        super().action()
