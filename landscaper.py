## character
player = {"money": 0, "tool": 0}


## tools
tools = [
    {"index": 0, "name": "teeth", "cost": 0, "pay": 1},
    {"index": 1, "name": "rusty scissors", "cost": 5, "pay": 5},
    {"index": 2, "name": "old push mower", "cost": 25, "pay": 50},
    {"index": 3, "name": "fancy battery-powered mower", "cost": 250, "pay": 100},
    {"index": 4, "name": "Team of Starving Students", "cost": 500, "pay": 250}
]


## Input
def playInput():
    result = input(
        "Welcome to landscaper! A game about cutting some grass! Do you want to [c]ut, [u]pgrade, or [q]uit? "
    )

    if result == "c":
        cut()

    if result == "u":
        upgrade()

    if result == "q":
        quit()
    
    

## cut
def cut():
    player["money"] += tools[player["tool"]]["pay"]
    print(f"You've made ${player['money']} using {tools[player['tool']]['name']}!")
    you_win()


## upgrade
def upgrade():
    if tools[player["tool"]]["index"] == 4:
        print("No more upgrades")
        you_win()
        
    if player["money"] < tools[player["tool"] + 1]["cost"]:
        print("You don't have enough money")
        you_win()
    else:
        player["money"] -= tools[player["tool"] + 1]["cost"]
        player["tool"] += 1
        print(f"You've got the {tools[player['tool']]['name']}!")
        you_win()

## quit
def quit():
    print("Game Over")


## win conditions
def you_win():
    if tools[player["tool"]]["index"] == 4 and player["money"] == 1000:
        print("You've won!")
        quit()
    else:
        playInput()

playInput()