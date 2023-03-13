import random
from Organism import Organism


class Plant (Organism):
    def __init__(self, world, strength, coordinates, age, newBorn, madeAction):
        super().__init__(world, strength, 0, coordinates, age, newBorn, madeAction)

    def action(self):
        if not self._newBorn:
            sewChance = random.randint(0, 99)
            if sewChance > 90:
                occupiedFields = self.checkWhatFieldsAreOccupied()
                placeForNewOrganism = self.findPlaceForNewOrganism(occupiedFields)
                if placeForNewOrganism.x != -1 and placeForNewOrganism.y != -1:
                    newOrg = self.createSameOrganism(placeForNewOrganism)
                    print("Sew was a success\n")
                    self.setMadeAction(True)
                    self._age += 1
                    return
                print("Sew not possible. Lack of space.\n")
                self.setMadeAction(True)

            print("Sew failed\n")
        self._age += 1
