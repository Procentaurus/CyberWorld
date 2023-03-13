import tkinter as tk
from tkinter import *
from Visuals.ChooseMenu import ChooseMenu
from Point import Point


class GameBoard:
    def __init__(self, world, sizeX, sizeY):
        self._world = world
        self._sizeX = sizeX
        self._sizeY = sizeY
        self._width = 1400
        self._height = 950
        self._startX = (self._width - self._sizeX * 30) / 2 - 100
        self._startY = 10

        root = tk.Tk()
        root.title("CYBER WORLD 2022 by Piotr Michalski")
        root.configure(bg="#c9c9c7")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        center_x = int(screen_width / 2 - self._width / 2)
        center_y = int(screen_height / 2 - self._height / 2)

        root.resizable(False, False)
        root.geometry(f'{self._width}x{self._height}+{center_x}+{center_y}')

        canvas = Canvas(root, bg="#c9c9c7", height=760, width=1300, bd=3, highlightbackground="#c9c9c7")
        canvas.place(x=50, y=130)

        self.printBorders(canvas)
        self.fillWithOrganisms(canvas)
        self.drawMenu(canvas)

        def saveAction():
            print("Save button pressed...")
            self._world.saveWorld()

        def loadAction():
            print("Load button pressed...")
            self._world.loadWorld()
            self.updateData(self._world.getSizeX(), self._world.getSizeY())

            canvas.create_polygon(0, 0, 1300, 0, 1300, 760, 0, 760, fill="#c9c9c7")
            self.printBorders(canvas)
            self.fillWithOrganisms(canvas)
            self.drawMenu(canvas)

        def turnAction():
            self._world.nextTurn()
            print("Next turn button clicked!")

            canvas.create_polygon(0, 0, 1300, 0, 1300, 760, 0, 760, fill="#c9c9c7")
            self.printBorders(canvas)
            self.fillWithOrganisms(canvas)
            self.drawMenu(canvas)

        saveButton = tk.Button(root, text="SAVE THE GAME", command=saveAction)
        loadButton = tk.Button(root, text="LOAD THE GAME", command=loadAction)
        turnButton = tk.Button(root, text="NEXT TURN", command=turnAction)

        saveButton.place(x=150, y=905, width=300, height=30)
        loadButton.place(x=550, y=905, width=300, height=30)
        turnButton.place(x=950, y=905, width=300, height=30)

        def motion(event):
            x, y = event.x, event.y
            if self._startX < x < self._sizeX * 30 + self._startX and self._startY < y < self._sizeY * 30 + self._startY:
                point = Point(int((x-self._startX)/30), int((y-self._startY)/30))
                if not self._world.isFieldOccupied(point):
                    ChooseMenu(x, y, self._startX, self._startY, self._world, canvas)

        canvas.bind('<Button-1>', motion)
        root.focus_set()
        root.bind("<Up>", self.up)
        root.bind("<Down>", self.down)
        root.bind("<Left>", self.left)
        root.bind("<Right>", self.right)
        root.bind('x', self.x)
        root.mainloop()

    def updateData(self, sizeX, sizeY):
        self._sizeX = sizeX
        self._sizeY = sizeY
        self._startX = (self._width - self._sizeX * 30) / 2 - 100

    def printBorders(self, canvas):

        canvas.create_line(self._startX - 1, self._startY - 1, self._startX + 30 * self._sizeX, self._startY - 1)
        canvas.create_line(self._startX - 1, self._startY - 1, self._startX - 1, self._startY + 30 * self._sizeY)
        canvas.create_line(self._startX + 30 * self._sizeX + 1, self._startY + 30 * self._sizeY - 1, self._startX - 1, self._startY + 30 * self._sizeY - 1)
        canvas.create_line(self._startX + 30 * self._sizeX + 1, self._startY + 30 * self._sizeY - 1, self._startX + 30 * self._sizeX + 1, self._startY + 1)

    def fillWithOrganisms(self, canvas):
        table = self._world.getOrganismsTable()
        for i in range(self._sizeX):
            for j in range(self._sizeY):
                if table[i][j] is not None:
                    color = table[i][j].color()
                    drawStartX = i * 30+self._startX
                    drawStartY = j * 30+self._startY
                    canvas.create_polygon(drawStartX, drawStartY, drawStartX+30, drawStartY, drawStartX+30, drawStartY+30, drawStartX, drawStartY+30, fill=color)

    def drawMenu(self, canvas):

        canvas.create_text(100, 740, text="Antelope", font="Times 14 italic bold")
        canvas.create_text(200, 740, text="Tortoise", font="Times 14 italic bold")
        canvas.create_text(300, 740, text="Human", font="Times 14 italic bold")
        canvas.create_text(400, 740, text="Wolf", font="Times 14 italic bold")
        canvas.create_text(500, 740, text="Sheep", font="Times 14 italic bold")
        canvas.create_text(600, 740, text="CyberSheep", font="Times 14 italic bold")
        canvas.create_text(700, 740, text="Fox", font="Times 14 italic bold")
        canvas.create_text(800, 740, text="WolfBerry", font="Times 14 italic bold")
        canvas.create_text(900, 740, text="Hogweed", font="Times 14 italic bold")
        canvas.create_text(1000, 740, text="Grass", font="Times 14 italic bold")
        canvas.create_text(1100, 740, text="Guarana", font="Times 14 italic bold")
        canvas.create_text(1200, 740, text="Dandelion", font="Times 14 italic bold")

        canvas.create_polygon(90, 690, 120, 690, 120, 720, 90, 720, fill="red")
        canvas.create_polygon(190, 690, 220, 690, 220, 720, 190, 720, fill="pink")
        canvas.create_polygon(290, 690, 320, 690, 320, 720, 290, 720, fill="blue")
        canvas.create_polygon(390, 690, 420, 690, 420, 720, 390, 720, fill="yellow")
        canvas.create_polygon(490, 690, 520, 690, 520, 720, 490, 720, fill="black")
        canvas.create_polygon(590, 690, 620, 690, 620, 720, 590, 720, fill="#b54e5d")
        canvas.create_polygon(690, 690, 720, 690, 720, 720, 690, 720, fill="orange")
        canvas.create_polygon(790, 690, 820, 690, 820, 720, 790, 720, fill="darkGray")
        canvas.create_polygon(890, 690, 920, 690, 920, 720, 890, 720, fill="gray")
        canvas.create_polygon(990, 690, 1020, 690, 1020, 720, 990, 720, fill="green")
        canvas.create_polygon(1090, 690, 1120, 690, 1120, 720, 1090, 720, fill="magenta")
        canvas.create_polygon(1190, 690, 1220, 690, 1220, 720, 1190, 720, fill="cyan")

    def up(self, event):
        print("Move for human: UP")
        self._world.setHumanMoveIndex(1)

    def down(self, event):
        print("Move for human: DOWN")
        self._world.setHumanMoveIndex(5)

    def left(self, event):
        print("Move for human: LEFT")
        self._world.setHumanMoveIndex(7)

    def right(self, event):
        print("Move for human: RIGHT")
        self._world.setHumanMoveIndex(3)

    def x(self, event):
        if not self._world.getIsSkillActivated() and self._world.getSkillDuration() == 0:
            self._world.setSkillActivation(True)
            print("You are IMMORTAL for 5 turns")
        elif not self._world.getIsSkillActivated() and self._world.getSkillDuration() > 0:
            print("You must wait for your skill to reload. Time remaining: " + str(1 + self._world.getSkillDuration()))
        elif self._world.getIsSkillActivated():
            print("Special ability is already in use. Time remaining: " + str(5 - self._world.getSkillDuration()))

