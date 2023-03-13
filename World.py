import random
from Point import Point

from Animals.Human import Human
from Animals.Sheep import Sheep
from Animals.CyberSheep import CyberSheep
from Animals.Fox import Fox
from Animals.Tortoise import Tortoise
from Animals.Wolf import Wolf
from Animals.Antelope import Antelope

from Plants.Dandelion import Dandelion
from Plants.Grass import Grass
from Plants.Hogweed import Hogweed
from Plants.WolfBerry import WolfBerry
from Plants.Guarana import Guarana



class World:
    def __init__(self, sizeX, sizeY):
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__turn = 0
        self.__isSkillActivated = False
        self.__skillDuration = 0
        self.__humanMoveIndex = -1
        self.__gameStatus = True
        self.__organismsTable = [[None for y in range(sizeY)] for x in range(sizeX)]
        self.__listOfAction = []
        self.__toRemove = []
        self.__toAdd = []
        self.__listOfHogweeds = []

    def setHumanMoveIndex(self, index):
        self.__humanMoveIndex = index

    def getHumanIndexMove(self):
        return self.__humanMoveIndex

    def getSkillDuration(self):
        return self.__skillDuration

    def getSizeX(self):
        return self.__sizeX

    def getSizeY(self):
        return self.__sizeY

    def getTurn(self):
        return self.__turn

    def getToRemove(self):
        return self.__toRemove

    def getListOfHogweeds(self):
        return self.__listOfHogweeds

    def getToAdd(self):
        return self.__toAdd

    def setTurn(self, turn):
        self.__turn = turn

    def getIsSkillActivated(self):
        return self.__isSkillActivated

    def setGameStatus(self):
        self.__gameStatus = False
    def placeOrganism(self, organism):
        x = organism.getPosition().x
        y = organism.getPosition().y
        if organism is not None and 0 <= x < self.__sizeX and 0 <= y < self.__sizeY:
            self.__organismsTable[x][y] = organism

    def deleteElement(self, coordinates):
        self.__organismsTable[coordinates.x][coordinates.y] = None

    def doesFieldExist(self, coordinates):
        if 0 <= coordinates.x < self.__sizeX and 0 <= coordinates.y < self.__sizeY:
            return True
        return False

    def isFieldOccupied(self, coordinates):
        if self.doesFieldExist(coordinates):
            if self.__organismsTable[coordinates.x][coordinates.y] is None:
                return False
            else:
                return True
        return False

    def findRandomBegginingPosition(self):
        newPosition = Point(random.randint(0, self.__sizeX - 1), random.randint(0, self.__sizeY - 1))

        while self.isFieldOccupied(newPosition):
            newPosition = Point(random.randint(0, self.__sizeX - 1), random.randint(0, self.__sizeY - 1))
        return newPosition

    def addToListInSuitablePlace(self, newOrg):
        if len(self.__listOfAction) == 0:
            self.__listOfAction.append(newOrg)
        else:
            added = False
            for org in self.__listOfAction:
                if newOrg.getInitiative() > org.getInitiative():
                    self.__listOfAction.insert(self.__listOfAction.index(org), newOrg)
                    added = True
                    break
                elif newOrg.getInitiative() == org.getInitiative() and newOrg.getAge() > org.getAge():
                    self.__listOfAction.insert(self.__listOfAction.index(org), newOrg)
                    added = True
                    break
            if not added:
                self.__listOfAction.append(newOrg)

    def add(self, newOrg):
        if newOrg is not None and 0 <= newOrg.getPosition().x < self.__sizeX and 0 <= newOrg.getPosition().y < self.__sizeY:
            self.__organismsTable[newOrg.getPosition().x][newOrg.getPosition().y] = newOrg
            if isinstance(newOrg, Hogweed):
                self.__listOfHogweeds.append(newOrg)

            if self.__turn == 0:
                self.addToListInSuitablePlace(newOrg)
            else:
                self.__toAdd.append(newOrg)

    def updateList(self):
        for org in self.__listOfAction:
            org.setMadeAction(False)
            org.setNewBorn()

    def deleteDeadOrganisms(self):
        for org in self.__toRemove:
            if org in self.__listOfAction:
                self.__listOfAction.remove(org)
            else:
                self.__toAdd.remove(org)
            if isinstance(org, Human):
                self.setGameStatus()
        self.__toRemove.clear()

    def copyFromListToList(self):
        for org in self.__toAdd:
            self.addToListInSuitablePlace(org)
        self.__toAdd.clear()

    def printList(self):
        for org in self.__listOfAction:
            org.draw()
            print(" {"+str(org.getPosition().x)+" "+str(org.getPosition().y)+"} ")
        print("\n")

    def setSkillActivation(self, flag):
        self.__isSkillActivated = flag

    def getOrganismsTable(self):
        return self.__organismsTable

    def nextTurn(self):
        self.__turn += 1
        self.printList()

        for org in self.__listOfAction:
            if org not in self.__toRemove and not org.getNewBorn():
                org.action()

        self.copyFromListToList()
        self.deleteDeadOrganisms()
        self.updateList()
        self.__humanMoveIndex -= 1

        if not self.__gameStatus:
            exit(0)
            print("GAME OVER\n")

        if self.getIsSkillActivated():
            self.__skillDuration += 1
        if self.__skillDuration == 5:
            self.setSkillActivation(False)
        if not self.getIsSkillActivated() and self.__skillDuration > 0:
            self.__skillDuration -= 1

    def saveWorld(self):
        self.updateList()
        self.deleteDeadOrganisms()

        file = open("loadedWorld.txt", "w")
        file.write(str(self.__sizeX) + ":" + str(self.__sizeY) + ":" + str(self.__turn) + ":" + str(self.__isSkillActivated) + ":" + str(self.__skillDuration) + ":" + str(len(self.__listOfAction))+"\n")
        for it in self.__listOfAction:
            file.write(it.getName() + ":" + str(it.getPosition().x) + ":" + str(it.getPosition().y) + ":" + str(it.getAge()) + ":" + str(it.getStrength()) + "\n")
        file.close()
        exit(0)

    def loadWorld(self):
        self.__listOfAction.clear()
        self.__toAdd.clear()
        self.__toRemove.clear()
        self.__listOfHogweeds.clear()

        file = open("loadedWorld.txt", "r")
        if file is None:
            return "Error occured while loading the file"

        data = file.readline()
        data = data.split(':')

        self.__sizeX = int(data[0])
        self.__sizeY = int(data[1])
        self.__turn = int(data[2])
        self.__isSkillActivated = bool(data[3])
        self.__skillDuration = int(data[4])
        self.__organismsTable = [[None for y in range(self.__sizeY)] for x in range(self.__sizeX)]
        number = int(data[5])

        for i in range(1, number+1):
            data = file.readline()
            data = data.split(':')
            _org = data[0]
            _x = int(data[1])
            _y = int(data[2])
            _age = int(data[3])
            _strength = int(data[4])
            point = Point(_x, _y)
            if _org == "Antelope":
                org = Antelope(self, point, _age, True, False, _strength)
            elif _org == "CyberSheep":
                org = org = CyberSheep(self, point, _age, True, False, _strength)
            elif _org == "Fox":
                org = Fox(self, point, _age, True, False, _strength)
            elif _org == "Human":
                org = Human(self, point, _age, True, False, _strength)
            elif _org == 'Sheep':
                org = Sheep(self, point, _age, True, False, _strength)
            elif _org == "Tortoise":
                org = Tortoise(self, point, _age, True, False, _strength)
            elif _org == 'Wolf':
                org = Wolf(self, point, _age,True, True, _strength)
            elif _org == "Guarana":
                org = Guarana(self, point, _age, True, False)
            elif _org == "Hogweed":
                org = Hogweed(self, point, _age, True, False)
            elif _org == "WolfBerry":
                org = WolfBerry(self, point, _age, True, False)
            elif _org == "Dandelion":
                org = Dandelion(self, point, _age, True, False)
            elif _org == "Grass":
                org = Grass(self, point, _age, True, False)
        file.close()
