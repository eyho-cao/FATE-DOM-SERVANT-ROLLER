import random
from Servant import Servant
from excelReader import readServants, getClassList

#global ServantsPool
servantsPool = []
servantClassList = getClassList()

def createServantsPool():
    for i in servantClassList:
        servantsPool.append(drawRandomServant(i))
    lastServant = random.choice(servantClassList)
    servantsPool.append(drawRandomServant(lastServant))

    return servantsPool


def drawRandomServant(servantClass):
    unfilteredServantsList = readServants(servantClass)
    uniqueServants = filterExistingServants(unfilteredServantsList)
    return random.choice(uniqueServants)


def filterExistingServants(unfilteredServantsPool):
    out = []
    for i in unfilteredServantsPool:
            isInList = False
            for j in servantsPool:
                if(i.servantName == j.servantName and i.servantClass == j.servantClass):
                    isInList = True
            if(not isInList):
                out.append(i)
    return out

def createTestPool():
    for i in range(8):
        tempServant = Servant(i, random.choice(servantClassList))
        servantsPool.append(tempServant)

def printServant(servant):
    print("Servant: ", servant.servantName, servant.servantClass)