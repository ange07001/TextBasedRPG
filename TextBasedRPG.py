import math
import json
import os

IsMainMenu = True

current_dir = os.path.dirname(os.path.abspath(__file__))
filename = 'save_data.json'
file_path = os.path.join(current_dir, filename)


save_data = {
    "mustang": {
        "color":"red",
        "year": 1962,
    },
    "f150": {
        "color": "blue",
        "year": 2005
    },
}


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
if os.path.exists(file_path):
    print("Save file already exists, loading save game...")
elif not os.path.exists(file_path):
    print("Save file does not exist or is corrupt, creating a new one...")

    with open(file_path, 'w') as json_file:
      json.dump(save_data, json_file, indent=3)

print("\n")

while IsMainMenu:
    try:
        mainMenu = int(input("Main Menu\n[1] Play\n[2] Exit\n"))
        if mainMenu == 1:
            Play = True
            IsMainMenu = False
        elif mainMenu == 2:
            Play = False
            IsMainMenu = False
        else:
            print(error)
    except ValueError:
        print(error)

class Player:
    def __init__(self, health, xp, speed, armor, damage):
        self.health = health
        self.xp = xp
        self.speed = speed
        self.armor = armor
        self.damage = damage

class Enemy:
    def __init__(self, health, level, speed, armor):
        self.health = health
        self.level = level
        self.speed = speed
        self.armor = armor




    