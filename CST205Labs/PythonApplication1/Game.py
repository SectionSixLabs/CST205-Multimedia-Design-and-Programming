
#LAB 11
#Strategy Game

#Global Variables and Arrays
WELCOME = "===================================================================================\n"

def getPlayerCommand():
    return input('Action: ')



def Game():
    inventory= []
    print (WELCOME)
    isExit=False
    while not isExit:
        actionInput= getPlayerCommand()
        isExit=True



Game()