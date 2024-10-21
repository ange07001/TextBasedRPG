import math
import json
import os
import sys

class Ansi:
    def Format(text, color):
        return "\033[0;" + color + "m" + text + "\033[0m"
    
    def Print(text, color):
        print(Ansi.Format(text,color))

    def reset():
        sys.stdout.write("\033[0m")

play = True
isMainMenu = True
isMenu = False
isInventory = False
isStats = False
isExplore = False
isForestoutskirtsDescription = False
isLocationForestOutskirts = False


Ansi.reset()

current_dir = os.path.dirname(os.path.abspath(__file__))
filename = 'save_data.json'
file_path = os.path.join(current_dir, filename)
error = Ansi.Format("\n" + "=" * 10 + "ERROR" + "=" * 10 + "\n","31") 

banner = """
 _____         _    ______                    _  ____________ _____ 
|_   _|       | |   | ___ \                  | | | ___ \ ___ \  __ \\
  | | _____  _| |_  | |_/ / __ _ ___  ___  __| | | |_/ / |_/ / |  \/
  | |/ _ \ \/ / __| | ___ \/ _` / __|/ _ \/ _` | |    /|  __/| | __ 
  | |  __/>  <| |_  | |_/ / (_| \__ \  __/ (_| | | |\ \| |   | |_\ \\
  \_/\___/_/\_\\__|  \____/ \__,_|___/\___|\__,_| \_| \_\_|    \____/

"""

print(banner)
print("#"*10 + " initializing " + "#"*10)

class Inventory:
    def remove(self,item,quantity,callError = False):
        if type(quantity) is int and quantity > 0:
            if item in save_game["inventory"]:
                if save_game["inventory"][item] > quantity:
                    save_game["inventory"][item] -= quantity
                elif save_game["inventory"][item] <= quantity:
                    del save_game["inventory"][item]
                saveGame()
            elif not item in save_game ["inventory"] and callError:
                Ansi.Print("Item is not in inventory","31")
        elif type(quantity) is not int or quantity <= 0 and callError: 
            Ansi.Print("Quantity is not valid","31")

class Player:
    def __init__(self, health, xp, speed, armor, damage):
        self.health = health
        self.xp = xp
        self.speed = speed
        self.armor = armor
        self.damage = damage

    def playerToDict(self):
        return {
            "health": self.health,
            "xp": self.xp,
            "speed": self.speed,
            "armor": self.armor,
            "damage": self.damage
        }

    @classmethod
    def dictToPlayer(cls, data):
        return cls(
            health=data["health"],
            xp=data["xp"],
            speed=data["speed"],
            armor=data["armor"],
            damage=data["damage"]
        )

def saveGame():
    state = save_game
    with open(file_path, "w") as f:
        json.dump(state, f, indent=3)

def loadGame():
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            save_game = data
            loadedPlayer = data["player"]
            player = Player.dictToPlayer(loadedPlayer)
            return(player,save_game)
    except FileNotFoundError:
        print("Save file was not found.")
    except json.JSONDecodeError:
        print("file was corrupted or not in proper JSON format.")  

class Enemy:
    def __init__(self, health, level, speed, armor):
        self.health = health
        self.level = level
        self.speed = speed
        self.armor = armor


inventory = Inventory()


if os.path.exists(file_path):
    print("Save file already exists, loading save game...")
    player, save_game = loadGame()
elif not os.path.exists(file_path):
    print("Save file does not exist or is corrupt, creating a new one...")
    player = Player(100, 0, 1, 0, 1)
    
    save_game = {
        "player": Player.playerToDict(player),

        "inventory": {
            "sword": 1,
            "apple": 1,
            "potion": 1,
        },
        "gameState": {
            "location": "swamps"
        },
        "stats": {
            "itemsLooted": 0,
            "enemiesDefeated": 0,
            "timesDied": 0,
        }
    }

    saveGame()

print("\n")



while play:
    while isMainMenu:
        try:
            mainMenuInput = int(input("\nMain Menu\n[1] Play\n[2] Exit\n"))
            if mainMenuInput == 1:
                isMenu = True
                isMainMenu = False
            elif mainMenuInput == 2:
                isMainMenu = False
                play = False
            else:
                print(error)
        except ValueError:
            print(error)

    while isMenu:
        try:
            menuInput = int(input("\n[1] Explore \n[2] Inventory \n[3] Stats\n[4] Exit\n"))
            match menuInput:
                case 1:
                    isExplore = True
                    isMenu = False
                case 2:
                    isInventory = True
                    isMenu = False
                case 3:
                    isStats = True 
                    isMenu = False
                case 4:
                    isMainMenu = True
                    isMenu = False
                case _:
                    print(error)
        except ValueError:
            print(error)

    while isInventory:
        try:
            for item, quantity in save_game["inventory"].items():
                print("-" * 25)
                print(f"{item}: {quantity}")
            isInventoryInput = int(input("\n[1] Discard item\n[2] Exit\n"))
            match isInventoryInput:
                case 1: 
                    item = input("Enter the item you want to discard: ")
                    quantity = int(input("Enter the quantity you want to discard: "))
                    inventory.remove(item,quantity,True)
                case 2:
                    isInventory = False
                    isMenu = True
                case _:
                    print(error)
        except ValueError:
            print(error)



    while isStats:
        print(f"\nTotal xp gained: {player.xp} xp")
        print(f"Items looted: {save_game['stats']['itemsLooted']} items")
        print(f"Enemies defeated: {save_game['stats']['enemiesDefeated']} enemies")
        print(f"Times died: {save_game['stats']['timesDied']} deaths")
        statsInput = int(input("\n[1] Exit\n"))
        if statsInput == 1:
            isStats = False
            isMenu = True
    while isExplore:
        try:
            exploreInput = int(input(f"\nChoose the location of your exploration\n{Ansi.Format('[1] Forest Outskirts','32')}\n[2] ?????\n[3] ?????\n[4] Exit\n"))
            match exploreInput:
                case 1:
                    isExplore = False
                    isForestoutskirtsDescription = True
                case 2|3:
                    Ansi.Print("\nThe location is not discoverd (or added)","33")
                case 4:
                    isExplore = False
                    isMenu = True
                case _:
                    print(error)
        except ValueError:
            print(error)
    while isForestoutskirtsDescription:
        try:
            Ansi.Print("\nForest Outskirts\n","32")
            forestoutskirtsDescriptionInput = int(input("""The Forest Outskirts is a dense and mysterious woodland located on the border of a thriving kingdom. Known for its thick,towering trees and ever-present mist,
the area is a blend of untamed wilderness and forgotten ruins. Ancient stone paths, hidden beneath years of undergrowth, crisscross the terrain.
The sound of distant creatures can be heard at all hours, and rumors abound of mystical artifacts lost in the forest’s depths.\n\n[1] Enter\n[2] Exit\n"""))
            match forestoutskirtsDescriptionInput:
                case 1:
                    isLocationForestOutskirts = True
                    isForestoutskirtsDescription = False
                case 2:
                    isMenu = True
                    isForestoutskirtsDescription = False
                case _:
                    print(error)
        except ValueError:
            print(error)
    
    ##while isLocationForestOutskirts:
