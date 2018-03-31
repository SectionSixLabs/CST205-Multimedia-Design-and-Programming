
#LAB 11
#Strategy Game

#Global Variables and Arrays
WELCOME = """
===================================================================================
|                                                                                 |
|                                                                                 |
|                                                                                 |
|                                                                                 |
|                                                                                 |
|                                                                                 |
===================================================================================
"""

def getPlayerCommand():
    return input('Action: ')

def processAction(action):
    #Processing Palyer Action
    if action in ['n', 'N']:
         print("Going North!")
    elif action in ['s', 'S']:
         print("Going South!")
    elif action in ['e', 'E']:
         print("Going East!")
    elif action in ['w', 'W']:
         print("Going West!")
    elif action in ['i', 'I']:
         print("Inventory:")
         for item in inventory:
             print('* ' + str(item))
    else:
         print("Invalid action!")

def Game():
    inventory= ['Spear','Knife','Healing Herbs']
    print (WELCOME)
    isExit=False
    while not isExit:
        actionInput= getPlayerCommand()
        processAction(actionInput)
        isExit=True



Game()