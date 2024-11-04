import os
import json
import utils


def saveGame():
    state = player
    with open(utils.playerJsonFilePath, "w") as f:
        json.dump(state, f, indent=3)

def loadGame():
    try:
        with open(utils.playerJsonFilePath, "r") as f:
            data = json.load(f)
            player = data
            return player
    except FileNotFoundError:
        print("Player save file was not found.")
    except json.JSONDecodeError:
        print("Player save file is corrupt or not in proper JSON format.")  

player = {
    "stats": {
        "itemsLooted": 0,
        "enemiesDefeated": 0,
        "timesDied": 0,
    },
    "attributes": {
        "health": 100,
        "speed": 100,
        "level": 1,
    },
    "inventory": {
        "stoneSword": 1,
        "potion": 5,
    }
}