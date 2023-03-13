import tkinter as tk
from Point import Point

from Animals.Fox import Fox
from Animals.Wolf import Wolf
from Animals.Sheep import Sheep
from Animals.Tortoise import Tortoise
from Animals.Antelope import Antelope
from Animals.CyberSheep import CyberSheep

from Plants.Grass import Grass
from Plants.WolfBerry import WolfBerry
from Plants.Dandelion import Dandelion
from Plants.Guarana import Guarana
from Plants.Hogweed import Hogweed


class ChooseMenu:
    def __init__(self, x, y, startX, startY, world, canvas):
        self._x = x
        self._y = y
        self._startX = startX
        self._startY = startY
        self._world = world
        self._canvas = canvas

        root = tk.Tk()
        root.title("Choose the animal to place: ")
        width = 170
        height = 240

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)

        root.resizable(False, False)
        root.geometry(f'{width}x{height}+{center_x}+{center_y}')

        point = Point(int((self._x-self._startX)/30), int((self._y-self._startY)/30))
        toDraw = Point(self._startX+point.x*30, self._startY+point.y*30)
        def placeFox():
            Fox(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x+30, toDraw.y, toDraw.x+30, toDraw.y+30, toDraw.x, toDraw.y+30, fill="orange")
            root.destroy()

        def placeSheep():
            Sheep(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x + 30, toDraw.y, toDraw.x + 30,toDraw.y + 30, toDraw.x,toDraw.y + 30, fill="black")
            root.destroy()

        def placeTortoise():
            Tortoise(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x + 30, toDraw.y, toDraw.x + 30, toDraw.y + 30, toDraw.x,toDraw.y + 30, fill="pink")
            root.destroy()

        def placeWolfBerry():
            WolfBerry(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x + 30, toDraw.y, toDraw.x + 30, toDraw.y + 30, toDraw.x,toDraw.y + 30, fill="darkGray")
            root.destroy()

        def placeDandelion():
            Dandelion(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x + 30, toDraw.y, toDraw.x + 30, toDraw.y + 30, toDraw.x,toDraw.y + 30, fill="cyan")
            root.destroy()

        def placeHogweed():
            Hogweed(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x + 30, toDraw.y, toDraw.x + 30, toDraw.y + 30, toDraw.x,toDraw.y + 30, fill="gray")
            root.destroy()

        def placeGrass():
            Grass(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x + 30, toDraw.y, toDraw.x + 30, toDraw.y + 30, toDraw.x,toDraw.y + 30, fill="green")
            root.destroy()

        def placeGuarana():
            Guarana(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x + 30, toDraw.y,toDraw.x + 30,toDraw.y + 30, toDraw.x,toDraw.y + 30, fill="magenta")
            root.destroy()

        def placeAntelope():
            Antelope(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x + 30, toDraw.y, toDraw.x + 30, toDraw.y + 30, toDraw.x,toDraw.y + 30, fill="red")
            root.destroy()

        def placeCyberSheep():
            CyberSheep(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x + 30, toDraw.y, toDraw.x + 30, toDraw.y + 30, toDraw.x,toDraw.y + 30, fill="#b54e5d")
            root.destroy()

        def placeWolf():
            Wolf(self._world, point, 0, True, True)
            canvas.create_polygon(toDraw.x, toDraw.y, toDraw.x + 30, toDraw.y, toDraw.x + 30, toDraw.y + 30, toDraw.x,toDraw.y + 30, fill="yellow")
            root.destroy()

        tk.Button(root, text="Antelope", command=placeAntelope).place(x=10, y=10, width=150, height=20)
        tk.Button(root, text="CyberSheep", command=placeCyberSheep).place(x=10, y=30, width=150, height=20)
        tk.Button(root, text="Fox", command=placeFox).place(x=10, y=50, width=150, height=20)
        tk.Button(root, text="Sheep", command=placeSheep).place(x=10, y=70, width=150, height=20)
        tk.Button(root, text="Tortoise", command=placeTortoise).place(x=10, y=90, width=150, height=20)
        tk.Button(root, text="Wolf", command=placeWolf).place(x=10, y=110, width=150, height=20)
        tk.Button(root, text="Grass", command=placeGrass).place(x=10, y=130, width=150, height=20)
        tk.Button(root, text="Dandelion", command=placeDandelion).place(x=10, y=150, width=150, height=20)
        tk.Button(root, text="Guarana", command=placeGuarana).place(x=10, y=170, width=150, height=20)
        tk.Button(root, text="Hogweed", command=placeHogweed).place(x=10, y=190, width=150, height=20)
        tk.Button(root, text="WolfBerry", command=placeWolfBerry).place(x=10, y=210, width=150, height=20)

        root.mainloop()

