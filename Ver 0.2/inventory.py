import player
import utils

def remove(item,quantity,returnToMenu,callError = False):
        if type(quantity) is int and quantity > 0:
            if item in player.player["inventory"]:
                if player.player["inventory"][item] > quantity:
                    player["inventory"][item] -= quantity
                elif player["inventory"][item] <= quantity:
                    del player["inventory"][item]
                if returnToMenu == True:
                    player.saveGame()
            elif not item in player.player ["inventory"] and callError:
                utils.Ansi.Print("Item is not in inventory","31")
        elif type(quantity) is not int or quantity <= 0 and callError: 
            utils.Ansi.Print("Quantity is not valid","31")