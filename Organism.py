import random
from abc import abstractmethod
import random
from Point import Point


class Organism:

    def __init__(self, world, strength, initiative, coordinates, age, newBorn, madeAction):
        self._age = age
        self._world = world
        self._initiative = initiative
        self._newBorn = newBorn
        self._madeAction = madeAction
        self._position = coordinates
        self._strength = strength

        self._world.add(self)

    @abstractmethod
    def createSameOrganism(self, coordinates):
        pass
    @abstractmethod
    def getName(self):
        pass
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def action(self):
        pass
    @abstractmethod
    def color(self):
        pass

    def setMadeAction(self, flag):
        self._madeAction = flag

    def checkWhatFieldsAreOccupied(self):
        fields = [-1]*8

        x = self._position.x
        y = self._position.y
        point = Point(x - 1, y - 1)
        if self._world.doesFieldExist(point) and not self._world.isFieldOccupied(point):
            fields[0] = 1
        point.changeNumbers(x, y - 1)
        if self._world.doesFieldExist(point) and not self._world.isFieldOccupied(point):
            fields[1] = 1
        point.changeNumbers(x+1, y - 1)
        if self._world.doesFieldExist(point) and not self._world.isFieldOccupied(point):
            fields[2] = 1
        point.changeNumbers(x+1, y)
        if self._world.doesFieldExist(point) and not self._world.isFieldOccupied(point):
            fields[3] = 1
        point.changeNumbers(x+1, y + 1)
        if self._world.doesFieldExist(point) and not self._world.isFieldOccupied(point):
            fields[4] = 1
        point.changeNumbers(x, y + 1)
        if self._world.doesFieldExist(point) and not self._world.isFieldOccupied(point):
            fields[5] = 1
        point.changeNumbers(x - 1, y + 1)
        if self._world.doesFieldExist(point) and not self._world.isFieldOccupied(point):
            fields[6] = 1
        point.changeNumbers(x - 1, y)
        if self._world.doesFieldExist(point) and not self._world.isFieldOccupied(point):
            fields[7] = 1

        return fields

    def wasAttackBlocked(self, attackingOrganism):
        return False

    def canItRun(self, attackingOrganism):
        return False

    def doesItHateHogweed(self):
        return False

    def doesItKillAnimalsAround(self):
        return False

    def isFightingDeadly(self):
        return False

    def canItStrengthen(self):
        return False

    def isItImmortal(self):
        return False

    def moveToNewPosition(self, placeForEscape):
        oldAnimal = self._position
        self.setPosition(placeForEscape)
        self._world.placeOrganism(self)
        self._world.deleteElement(oldAnimal)

    def findPlaceForNewOrganism(self, indexTable):
        number = 0
        for i in range(8):
            if indexTable[i] == 1 :
                number += 1
                indexTable[i] = i

        point = Point(0, 0)
        if number != 0:
            directionTable = [0]*number
            index = 0
            for i in range(8):
                if indexTable[i] != -1:
                    directionTable[index] = indexTable[i]
                    index += 1

            direction = directionTable[random.randint(0, number-1)]
            if direction == 0:
                point.changeNumbers(self._position.x - 1, self._position.y - 1)
            if direction == 1:
                point.changeNumbers(self._position.x, self._position.y - 1)
            if direction == 2:
                point.changeNumbers(self._position.x + 1, self._position.y - 1)
            if direction == 3:
                point.changeNumbers(self._position.x + 1, self._position.y)
            if direction == 4:
                point.changeNumbers(self._position.x + 1, self._position.y + 1)
            if direction == 5:
                point.changeNumbers(self._position.x, self._position.y + 1)
            if direction == 6:
                point.changeNumbers(self._position.x - 1, self._position.y + 1)
            if direction == 7:
                point.changeNumbers(self._position.x - 1, self._position.y)
        else:
            point.changeNumbers(- 1, -1)

        return point

    def getStrength(self):
        return self._strength

    def getInitiative(self):
        return self._initiative

    def setPosition(self, position):
        self._position = position

    def getPosition(self):
        return self._position

    def getAge(self):
        return self._age

    def getNewBorn(self):
        return self._newBorn

    def getMadeAction(self):
        return self._madeAction

    def setNewBorn(self):
        self._newBorn = False
