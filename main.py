import random
from createServantsPool import createServantsPool, drawMiyuServants

servantsPool = []
numPlayers = None

def runProgram():
    run = True
    while run:
        userInput = input('Enter Command: \n')
        handleCommand(userInput.split())

def handleCommand(input):
    if(len(input) <= 0):
        print('Please enter a command: use \'help\' for list of commands')
        return
    cmd = input[0]
    if cmd == 'help':
        None
    elif cmd == 'create':
        global servantsPool
        servantsPool = createServantsPool()
        print('Servant Pool Created\n---------------------')
    elif cmd == 'miyu':
        if(len(servantsPool) <= 0):
            print('ERROR: Please create regular servant pool first\n---------------------')
            return
        servants = drawMiyuServants(servantsPool)
        printServantPool(servants)
    elif cmd == 'numPlayers' or cmd == 'numplayers':
        if(len(cmd) < 2):
            print('ERROR: Missing parameters. Expected usage: \'numPlayers (# of players)\'\n---------------------')
            return
        elif(not input[1].isdigit() and (int(input[1]) > 1)):
            print('ERROR: Unexpected input. Expected integer > 1\n---------------------')
            return
        global numPlayers
        numPlayers = int(input[1])
        print('Number of players set to:', numPlayers,'\n---------------------')
    elif cmd == 'draw':
        if(numPlayers is None):
            print('ERROR: Please input number of players first\n---------------------')
            return
        elif(len(servantsPool) <= 0):
            print('ERROR: Please create regular servant pool first\n---------------------')
            return
        distributeServants()
    elif cmd == 'clearPool' or cmd == 'clearpool':
        global servantsPool
        servantsPool = []
        print('Servant Pool Cleared')
    else:
        print('ERROR: Command not found: use \'help\' for list of commands\n---------------------')

def distributeServants():
    for i in range(numPlayers-1):
            selectedServant = drawPlayerServant()
            displayServant(selectedServant)
            print('\n' * 100)
    print('---------------------\nFinished drawing player servants')
def drawPlayerServant():
    servant = random.choice(servantsPool)
    servantsPool.remove(servant)
    return servant

def displayServant(servant):
    print('---------------------\nYour servant is: ')
    printServant(servant)
    print('---------------------\n\n')
    waitForInput = input('Press enter to clear console and continue:')

def printServant(servant):
        print("Servant:", servant.servantName, ' || Class:', servant.servantClass)

def printServantPool(pool):
    for i in pool:
        print("Servant:", i.servantName, ' || Class:', i.servantClass)

runProgram()