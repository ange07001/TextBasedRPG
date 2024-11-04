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
    print(player.player)
elif not os.path.exists(utils.playerJsonFilePath):
    utils.Ansi.Print("Save file does not exist or is corrupt, creating a new one...", "33")
    player.saveGame()

