# Utility functions for the game
import sys
import os
class Ansi:
    def Format(text, color):
        return "\033[0;" + color + "m" + text + "\033[0m"
    
    def Print(text, color):
        print(Ansi.Format(text,color))

    def reset():
        sys.stdout.write("\033[0m")

banner = """
 _____         _    ______                    _  ____________ _____ 
|_   _|       | |   | ___ \                  | | | ___ \ ___ \  __ \\
  | | _____  _| |_  | |_/ / __ _ ___  ___  __| | | |_/ / |_/ / |  \/
  | |/ _ \ \/ / __| | ___ \/ _` / __|/ _ \/ _` | |    /|  __/| | __ 
  | |  __/>  <| |_  | |_/ / (_| \__ \  __/ (_| | | |\ \| |   | |_\ \\
  \_/\___/_/\_\\__|  \____/ \__,_|___/\___|\__,_| \_| \_\_|    \____/

"""

error = Ansi.Format("\n" + "=" * 10 + "ERROR" + "=" * 10 + "\n","31") 

currentDir = os.path.dirname(os.path.abspath(__file__))

playerJsonFilename = 'player.json'
playerJsonFilePath = os.path.join(currentDir, playerJsonFilename)

itemsFilename = 'items.json'
itemsFilePath = os.path.join(currentDir, itemsFilename)

worldFilename = 'world.json'
worldFilePath = os.path.join(currentDir, worldFilename)