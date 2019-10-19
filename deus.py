#!/usr/bin/env python3

from deus.main_window   import MainWindow
from deus.world         import World

def main():
    world = World()
    mainWindow = MainWindow(640, 480, "Deus", world)

if __name__ == "__main__":
    main()
