from openpyxl import load_workbook
import Servant

def readServants(servantClass): 
    wb = load_workbook(filename='Servants.xlsx')
    ws = wb[servantClass]
    outList = []
    for i in ws.rows:
        rowValue = i["A"]
        if rowValue == 'Servant name':
            continue
        servant = Servant(rowValue, servantClass)
        outList.append(servant)
    
    return outList
