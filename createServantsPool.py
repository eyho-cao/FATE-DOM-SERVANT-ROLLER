import random
from Servant import Servant
from excelReader import readServants, getClassList

#global ServantsPool
servantsPool = []
servantClassList = getClassList()

def createServantsPool():
    for i in servantClassList:
        servantsPool.append(drawRandomServantFromClass(i, servantsPool))
    last = selectRandomClass()
    servantsPool.append(drawRandomServantFromClass(last, servantsPool))

    return servantsPool

def selectRandomClass():
    return random.choice(servantClassList)

def drawRandomServantFromClass(servantClass, compiledPool):
    unfilteredServantsList = readServants(servantClass)
    uniqueServants = filterExistingServants(unfilteredServantsList, compiledPool)
    return random.choice(uniqueServants)

def filterExistingServants(unfilteredServantsPool, compiledPool):
    out = []
    for i in unfilteredServantsPool:
            isInList = isServantInPool(i, compiledPool)
            if(not isInList):
                out.append(i)
    return out

def isServantInPool(servant, pool):
    for i in pool:
        if(i.servantName == servant.servantName and i.servantClass == servant.servantClass):
            return True

def drawRandomServant():
    servantClass = selectRandomClass()
    servant = drawRandomServantFromClass(servantClass)
    return servant

def drawMiyuServants(usedPool):
    miyuPool = []
    for i in range(3):
        servantUsed = True
        servant = None
        while servantUsed:
            servantClass = selectRandomClass()
            servant = drawRandomServantFromClass(servantClass)
            if(not isServantInPool(servant, usedPool)):
                servantUsed = False
        if(servant):
            miyuPool.append(servant)
        else:
            print('Something went wrong and no valid servant was selected')
    return miyuPool

            
            

def createTestPool():
    for i in range(8):
        tempServant = Servant(i, random.choice(servantClassList))
        servantsPool.append(tempServant)

def printServant(servant):
    print("Servant: ", servant.servantName, servant.servantClass)

def printServantPool(servantsPool):
    for i in servantsPool:
        print("Servant:", i.servantName, ' || Class:', i.servantClass)