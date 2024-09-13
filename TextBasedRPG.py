import math
import json
import os

isMainMenu = True

current_dir = os.path.dirname(os.path.abspath(__file__))
filename = 'save_data.json'
file_path = os.path.join(current_dir, filename)

error = "\n" + "=" * 10 + "ERROR" + "=" * 10 + "\n"

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


if os.path.exists(file_path):
    print("Save file already exists, loading save game...")
    player, save_game = loadGame()
elif not os.path.exists(file_path):
    print("Save file does not exist or is corrupt, creating a new one...")
    player = Player(100, 0, 1, 0, 1)
    
    save_game = {
        "player": Player.playerToDict(player),

        "gameState": {
            "location": "swamps"
        },
        "stats": {
            "xpGained": 500
        }
    }

    saveGame()

print("\n")

while isMainMenu:
    try:
        mainMenu = int(input("Main Menu\n[1] Play\n[2] Exit\n"))
        if mainMenu == 1:
            play = True
            isMainMenu = False
        elif mainMenu == 2:
            play = False
            isMainMenu = False
        else:
            print(error)
    except ValueError:
        print(error)