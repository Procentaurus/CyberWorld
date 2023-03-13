import tkinter as tk
from Visuals.GameBoard import GameBoard
from World import World

from Animals.Human import Human
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


class StartMenu:

    def __init__(self):
        root = tk.Tk()
        root.title("Set the size of the board")
        window_width = 170
        window_height = 200

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        root.resizable(False, False)
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # SizeX Entry
        width_label = tk.Label(root, text="Write down the sizeX")
        width_label.place(x=10, y=10, width=150, height=20)

        width_entry = tk.Entry(root)
        width_entry.place(x=10, y=40, width=150, height=20)
        width_entry.insert(0, "10")

        # SizeY Entry
        height_label = tk.Label(root, text="Write down the sizeY")
        height_label.place(x=10, y=80, width=150, height=20)

        height_entry = tk.Entry(root)
        height_entry.place(x=10, y=110, width=150, height=20)
        height_entry.insert(0, "10")

        def start_clicked():
            sizeX = int(width_entry.get())
            sizeY = int(height_entry.get())

            world = World(sizeX, sizeY)  # creating new world

            # creating all default animals
            WolfBerry(world, world.findRandomBegginingPosition(), 0, False, False)
            Wolf(world, world.findRandomBegginingPosition(), 0, False, False)
            Wolf(world, world.findRandomBegginingPosition(), 0, False, False)
            Grass(world, world.findRandomBegginingPosition(), 0, False, False)
            Grass(world, world.findRandomBegginingPosition(), 0, False, False)
            Dandelion(world, world.findRandomBegginingPosition(), 0, False, False)
            Antelope(world, world.findRandomBegginingPosition(), 0, False, False)
            Human(world, world.findRandomBegginingPosition(), 0, False, False)
            Tortoise(world, world.findRandomBegginingPosition(), 0, False, False)
            Guarana(world, world.findRandomBegginingPosition(), 0, False, False)
            Hogweed(world, world.findRandomBegginingPosition(), 0, False, False)
            Fox(world, world.findRandomBegginingPosition(), 0, False, False)
            Sheep(world, world.findRandomBegginingPosition(), 0, False, False)
            Sheep(world, world.findRandomBegginingPosition(), 0, False, False)
            Wolf(world, world.findRandomBegginingPosition(), 0, False, False)
            CyberSheep(world, world.findRandomBegginingPosition(), 0, False, False)

            root.withdraw()
            GameBoard(world, sizeX, sizeY)

        start_button = tk.Button(root, text="OK", command=start_clicked)
        start_button.place(x=10, y=170, width=150, height=20)

        root.mainloop()
