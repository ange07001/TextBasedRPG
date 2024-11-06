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
                exit()
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
                    Explore()
                    break
                case 2:
                    Inventory()
                    break
                case 3:
                    Stats()
                    break
                case 4:
                    MainMenu()
                    break
                case _:
                    print(utils.error)
        except ValueError:
            print(utils.error)

def Explore():
    while True:
        try:
            exploreInput = int(input(f"\nChoose the location of your exploration\n{utils.Ansi.Format('[1] Forest Outskirts','32')}\n[2] ?????\n[3] ?????\n[4] Exit\n"))
            match exploreInput:
                case 1:
                    ForestoutskirtsDescription()
                    break
                case 2|3:
                    utils.Ansi.Print("\nThe location is not discoverd (or added)","33")
                case 4:
                    Menu()
                    break
                case _:
                    print(utils.error)
        except ValueError:
            print(utils.error)

def ForestoutskirtsDescription():
    while True:
        try:
            utils.Ansi.Print("\nForest Outskirts\n","32")
            forestoutskirtsDescriptionInput = int(input("""The Forest Outskirts is a dense and mysterious woodland located on the border of a thriving kingdom. Known for its thick,towering trees and ever-present mist,
the area is a blend of untamed wilderness and forgotten ruins. Ancient stone paths, hidden beneath years of undergrowth, crisscross the terrain.
The sound of distant creatures can be heard at all hours, and rumors abound of mystical artifacts lost in the forest’s depths.\n\n[1] Enter\n[2] Exit\n"""))
            match forestoutskirtsDescriptionInput:
                case 1:
                    break
                case 2:
                    Explore()
                    break
                case _:
                    print(utils.error)
        except ValueError:
            print(utils.error)

def Stats():
    while True:
        print(f"\nTotal xp gained: {player.player['attributes']['xp']} xp")
        print(f"Items looted: {player.player['stats']['itemsLooted']} items")
        print(f"Enemies defeated: {player.player['stats']['enemiesDefeated']} enemies")
        print(f"Times died: {player.player['stats']['timesDied']} deaths")
        statsInput = int(input("\n[1] Exit\n"))
        if statsInput == 1:
            Menu()
            break

def Inventory(returnToMenu = False):
    while True:
        try:
            maxItemLen = len("Item")
            maxQuantityLen = len("Quantity")
            
            # Calculate the maximum lengths for item names and quantities
            for item, quantity in player.player["inventory"].items:
                if len(item) > maxItemLen:
                    maxItemLen = len(item)
                if len(str(quantity)) > maxQuantityLen:
                    maxQuantityLen = len(str(quantity))
            
            extraLen = 3
            header = f"|{'Item':<{maxItemLen + extraLen}}|{'Quantity':>{maxQuantityLen + extraLen}}|"
            line = len(header) * "-"
            
            print("\n")
            print(line)
            print(header)
            print(line)
            for item, quantity in player.player["inventory"].items():
                print(f"|{item:<{maxItemLen + extraLen}}|{quantity:>{maxQuantityLen + extraLen}}|")
            print(line)
            
            isInventoryInput = int(input("\n[1] Discard item\n[2] Exit\n"))
            match isInventoryInput:
                case 1: 
                    item = input("Enter the item you want to discard: ")
                    quantity = int(input("Enter the quantity you want to discard: "))
                    inventory.remove(item, quantity,returnToMenu, True)
                case 2:
                    if returnToMenu == False:
                        break
                    elif returnToMenu == True:
                        Menu()
                        break
                case _:
                    print(utils.error)
        except ValueError:
            print(utils.error)


MainMenu()