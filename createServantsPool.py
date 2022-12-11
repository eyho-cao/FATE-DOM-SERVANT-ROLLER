import random
from Servant import Servant
from constants import CLASS_LIST
from excelReader import readServants

#global ServantsPool
servantsPool = []
servantClassList = CLASS_LIST

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
        if(len(servantsPool) > 0):
            for j in servantsPool:
                if(not (i.servantName == j.servantName and i.servantClass == j.servantClass)):
                    out.append(i)
        else:
            out.append(i)
    return out

def createTestPool():
    for i in range(8):
        tempServant = Servant(i, random.choice(servantClassList))
        servantsPool.append(tempServant)

def printServantPool():
    for i in servantsPool:
        print("Servant:", i.servantName, ' || Class:', i.servantClass)

def printServant(servant):
    print("Servant: ", servant.servantName, servant.servantClass)