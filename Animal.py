import random
from abc import abstractmethod
from Organism import Organism
from Point import Point


class Animal(Organism):

    def __init__(self, world, strength, initiative, position, age, newBorn, madeAction):
        super().__init__(world, strength, initiative, position, age, newBorn, madeAction)
    @abstractmethod
    def getName(self):
        pass
    @abstractmethod
    def draw(self):
        pass

    def doSpeciesMatch(self, organism):
        if self._world.doesFieldExist(self._position):
            if self.getName() == organism.getName():
                return True
            else:
                return False
        return False

    def breed(self):
        table = self.checkWhatFieldsAreOccupied()
        newPlace = self.findPlaceForNewOrganism(table)
        if newPlace.x != -1 and newPlace.y != -1:
            newOrg = self.createSameOrganism(newPlace)
            print(" Breeding succeeded. Baby is in {"+str(newOrg.getPosition().x)+","+str(newOrg.getPosition().y)+"}\n")
        else:
            print(" Breeding failed. No space for baby. \n")

    def getIndexOfMove(self):
        sizeX = self._world.getSizeX()
        sizeY = self._world.getSizeY()
        crdX = self._position.x
        crdY = self._position.y

        if crdY == 0 and crdX == 0: return random.randint(0, 2)+3;
        elif crdY == 0 and 0 < crdX < sizeX - 1: return random.randint(0, 4) + 3;
        elif crdY == 0 and crdX == sizeX -1: return random.randint(0, 2)+5;
        elif crdX == 0 and 0 < crdY < sizeY - 1: return random.randint(0, 4) + 1;
        elif sizeY - 1 > crdY > 0 and sizeX - 1 > crdX > 0: return random.randint(0, 7);
        elif crdX == sizeX -1 and 0 < crdY < sizeY - 1:
            indexOfMove = random.randint(0, 4)
            if indexOfMove > 1:
                indexOfMove += 3
            return indexOfMove
        elif crdX == 0 and crdY == sizeY - 1: return random.randint(0, 2)+1;
        elif 0 < crdX < sizeX -1 and crdY == sizeY-1:
            indexOfMove = random.randint(0, 4)
            if indexOfMove == 4:
                indexOfMove += 3
            return indexOfMove
        elif crdX == sizeX - 1 and crdY == sizeY -1:
            indexOfMove = random.randint(0, 2)
            if indexOfMove == 2:
                indexOfMove += 5
            return indexOfMove
        else:
            return 0

    def move(self, indexOfMove):
        posX = self._position.x
        posY = self._position.y
        if indexOfMove == 0:
            self._position.x -= 1
            self._position.y -=1
        elif indexOfMove == 1:
            self._position.y -=1
        elif indexOfMove == 2:
            self._position.x +=1
            self._position.y -=1
        elif indexOfMove == 3:
            self._position.x +=1
        elif indexOfMove == 4:
            self._position.x +=1
            self._position.y +=1
        elif indexOfMove == 5:
            self._position.y +=1
        elif indexOfMove == 6:
            self._position.x -=1
            self._position.y +=1
        elif indexOfMove == 7:
            self._position.x -=1

        self.draw()
        print(" {"+str(posX)+"."+str(posY)+"} moved with index "+str(indexOfMove)+"\n")
        self._world.placeOrganism(self)
        point = Point(posX, posY)
        self._world.deleteElement(point)

    def action(self):
        if not self._madeAction and not self._newBorn:
            indexOfmove = self.getIndexOfMove()
            point = Point(0, 0)
            table = self._world.getOrganismsTable()

            if indexOfmove == 0:
                point.changeNumbers(self._position.x - 1, self._position.y - 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x - 1][self._position.y - 1])

            elif indexOfmove == 1:
                point.changeNumbers(self._position.x, self._position.y - 1)
                if not self._world.isFieldOccupied(point): self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x][self._position.y - 1])
            elif indexOfmove == 2:
                point.changeNumbers(self._position.x + 1, self._position.y - 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x + 1][self._position.y - 1])
            elif indexOfmove == 3:
                point.changeNumbers(self._position.x + 1, self._position.y)
                if not self._world.isFieldOccupied(point):
                        self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x + 1][self._position.y])
            elif indexOfmove == 4:
                point.changeNumbers(self._position.x + 1, self._position.y + 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x + 1][self._position.y + 1])
            elif indexOfmove == 5:
                point.changeNumbers(self._position.x, self._position.y + 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x][self._position.y + 1])

            elif indexOfmove == 6:
                point.changeNumbers(self._position.x - 1, self._position.y + 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x - 1][self._position.y + 1])

            elif indexOfmove == 7:
                point.changeNumbers(self._position.x - 1, self._position.y)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x - 1][self._position.y])

            self._age +=1

    def collision(self, collidingOrganism):
        if self.doSpeciesMatch(collidingOrganism):
            print("Breeding process: {"+str(self._position.x)+"," + str(self._position.y)+" and {" +str(collidingOrganism.getPosition().x)+","+str(collidingOrganism.getPosition().y)+"}\n")
            if not collidingOrganism.getMadeAction() and not collidingOrganism.getNewBorn():
                self.breed()
                self.setMadeAction(True)
                collidingOrganism.setMadeAction(True)

        else:
            targetCoordinates = collidingOrganism.getPosition()
            toRemove = self._world.getToRemove()
            noDeath = False
            if collidingOrganism.wasAttackBlocked(self):
                print("T pushed an attack from {"+str(self._position.x)+","+str(self._position.y)+"} back.\n")
            elif collidingOrganism.canItRun(self):
                table = self.checkWhatFieldsAreOccupied()
                placeForEscape = self.findPlaceForNewOrganism(table)
                if placeForEscape.x != -1 and placeForEscape.y != -1:

                    collidingOrganism.moveToNewPosition(placeForEscape)
                    self.moveToNewPosition(targetCoordinates)

                    collidingOrganism.draw()
                    print(" was attacked by stronger enemy and run. New position: {"+str(collidingOrganism.getPosition().x) + "," + str(collidingOrganism.getPosition().y)+"} \n")
                else:
                    if collidingOrganism.isItImmortal():
                        collidingOrganism.draw()
                        print(" {"+str(collidingOrganism.getPosition().x)+","+str(collidingOrganism.getPosition().y)+"} was attacked by stronger enemy, but there was no space for run. Human survived attack in its old position.\n")

            elif self.isItImmortal() and collidingOrganism.getStrength() > self._strength:
                table = collidingOrganism.checkWhatFieldsAreOccupied()
                placeForEscape = collidingOrganism.findPlaceForNewOrganism(table)
                if placeForEscape.x != -1 and placeForEscape.y != -1:
                    self.moveToNewPosition(placeForEscape)
                    print("You attacked stronger enemy, but survived and withdrew, because of immortality. You are now in position {"+str(self._position.x)+","+ str(self._position.y)+"} \n")
                    return
                print("You were attacked by stronger enemy, but you survived, because of immortality. You are still in position {"+str(collidingOrganism.getPosition().x)+","+ str(collidingOrganism.getPosition().y)+"} \n")
            elif self._strength >= collidingOrganism.getStrength(): # wygrana orgamnizmu
                if collidingOrganism.canItStrengthen():
                    self._strength += 3
                    self.draw()
                    print(" {"+str(self._position.x)+"," + str(self._position.y) + "} ate guarana and became stronger. \n")
                    noDeath = True
                elif collidingOrganism.doesItKillAnimalsAround():
                    self._world.getListOfHogweeds().remove(collidingOrganism)

                if not noDeath:
                    self.draw()
                    print(" {"+str(self._position.x)+"," + str(self._position.y)+"} killed {"+str(collidingOrganism.getPosition().x)+"," + str(collidingOrganism.getPosition().y)+"} ")
                    collidingOrganism.draw()
                    print("\n")

                self._world.deleteElement(targetCoordinates)
                toRemove.append(collidingOrganism)
                self.moveToNewPosition(targetCoordinates)

            else: #przegrana organizmu i jego śmierć
                if collidingOrganism.isFightingDeadly():
                    self._world.deleteElement(targetCoordinates)
                    toRemove.append(collidingOrganism)
                self.draw()
                print(" {" + str(self._position.x) + "," + str(self._position.y) + "} died during attack on {" + str(collidingOrganism.getPosition().x)+"," + str(collidingOrganism.getPosition().y) + "}\n" )
                self._world.deleteElement(self._position)
                toRemove.append(self)

    def tranformIntoMoveIndex(self, coordinates):
        x = coordinates.x - self._position.x
        y = coordinates.y - self._position.y

        if x == -1 and y == -1:
            return 0
        elif x == 0 and y == -1:
            return 1
        elif x == 1 and y == -1:
            return 2
        elif x == 1 and y == 0:
            return 3
        elif x == 1 and y == 1:
            return 4
        elif x == 0 and y == 1:
            return 5
        elif x == -1 and y == 1:
            return 6
        elif x == -1 and y == 0:
            return 7
        else:
            return -1

    def actionWithIndex(self, indexOfmove):
        table = self._world.getOrganismsTable()
        if not self._madeAction and not self._newBorn:
            point = Point(0, 0)

            if indexOfmove == 0:
                point.changeNumbers(self._position.x - 1, self._position.y - 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x - 1][self._position.y - 1])

            elif indexOfmove == 1:
                point.changeNumbers(self._position.x, self._position.y - 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x][self._position.y - 1])

            elif indexOfmove == 2:
                point.changeNumbers(self._position.x + 1, self._position.y - 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x + 1][self._position.y - 1])

            elif indexOfmove == 3:
                point.changeNumbers(self._position.x + 1, self._position.y)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x + 1][self._position.y])

            elif indexOfmove == 4:
                point.changeNumbers(self._position.x + 1, self._position.y + 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x + 1][self._position.y + 1])

            elif indexOfmove == 5:
                point.changeNumbers(self._position.x, self._position.y + 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x][self._position.y + 1])

            elif indexOfmove == 6:
                point.changeNumbers(self._position.x - 1, self._position.y + 1)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x - 1][self._position.y + 1])

            elif indexOfmove == 7:
                point.changeNumbers(self._position.x - 1, self._position.y)
                if not self._world.isFieldOccupied(point):
                    self.move(indexOfmove)
                else:
                    self.collision(table[self._position.x - 1][self._position.y])

            self._age += 1
