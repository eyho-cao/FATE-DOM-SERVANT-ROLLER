import random
import Servant
from constants import CLASS_LIST
from excelReader import readServants

#global ServantsPool
servantsPool = []
servantClassList = CLASS_LIST

def createServantsPool():
    for i in range(servantClassList):
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
        for j in servantsPool:
            if(not (i.servantName == j.servantName and i.servantClass ==j.servantClass)):
                out.append(i)
    return out