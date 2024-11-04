import json
import os
import sys

import utils
import player
import inventory

print(utils.banner)
print("#"*10 + " initializing " + "#"*10)

# checking dependencies
if os.path.exists(utils.itemsFilePath) and os.path.exists(utils.worldFilePath):
    utils.Ansi.Print("All JSON dependencies exist...", "32")
elif not os.path.exists(utils.itemsFilePath) or not os.path.exists(utils.worldFilePath):
    utils.Ansi.Print("Some or all JSON dependencies are missing or corrupt...", "31")

# loading player save
if os.path.exists(utils.playerJsonFilePath):
    utils.Ansi.Print("Save file already exists, loading save game...", "32")
    player.player = player.loadGame()
elif not os.path.exists(utils.playerJsonFilePath):
    utils.Ansi.Print("Save file does not exist or is corrupt, creating a new one...", "33")
    player.saveGame()

def MainMenu():
    while True:
        try:
            mainMenuInput = int(input("\nMain Menu\n[1] Play\n[2] Exit\n"))
            if mainMenuInput == 1:
                Menu()
            elif mainMenuInput == 2:
                break
            else:
                print(utils.error)
        except ValueError:
            print(utils.error)

def Menu():
    while True:
        try:
            print("\nMenu")
            menuInput = int(input("[1] Explore \n[2] Inventory \n[3] Stats\n[4] Exit\n"))
            match menuInput:
                case 1:
                    break
                case 2:
                    break
                case 3:
                    break
                case 4:
                    MainMenu()
                case _:
                    print(utils.error)
        except ValueError:
            print(utils.error)



MainMenu()