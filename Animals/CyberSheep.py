import math
from Point import Point
from Animal import Animal


class CyberSheep(Animal):

    def __init__(self, world, position, age, newBorn, madeAction, strength=11):
        super().__init__(world, strength, 4, position, age, newBorn, madeAction)

    def draw(self):
        print("C")

    def createSameOrganism(self, coordinates):
        return CyberSheep(self._world, coordinates, 1, True, True)

    def getName(self):
        name = "CyberSheep"
        return name

    def color(self):
        return "#b54e5d"

    def action(self):
        newPos = Point(self._position.x, self._position.y)
        if len(self._world.getListOfHogweeds()) > 0:
            closestHogweed = None
            closestDistance = 1000
            for org in self._world.getListOfHogweeds():
                dist = self.getDistance(org)
                if dist < closestDistance:
                    closestHogweed = org
                    closestDistance = dist
            if closestHogweed is not None:
                direction = Point(self._position.x - closestHogweed.getPosition().x, self._position.y - closestHogweed.getPosition().y)
                if direction.x > 0:
                    newPos.x -= 1
                elif direction.x < 0:
                    newPos.x += 1
                if direction.y > 0:
                    newPos.y -= 1
                elif direction.y < 0:
                    newPos.y += 1
            moveIndex = self.tranformIntoMoveIndex(newPos)
            super().actionWithIndex(moveIndex)
        else:
            super().action()

    def getDistance(self, org):
        x = abs(self._position.x - org.getPosition().x)
        y = abs(self._position.y - org.getPosition().y)
        distance = math.sqrt(x**2 + y**2)
        return distance

    def doesItHateHogweed(self):
        return True

