import math
import json



IsMainMenu = True
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

while IsMainMenu:
    try:
        mainMenu = int(input("Main Menu\n1. Play\n2. Exit\n"))
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




    