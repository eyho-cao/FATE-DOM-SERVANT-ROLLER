from openpyxl import load_workbook
from Servant import Servant

def readServants(servantClass): 
    wb = load_workbook(filename='Servants.xlsx')
    ws = wb[servantClass]
    outList = []
    for row in ws.iter_rows(min_row=2, min_col=1):
        servant = Servant(row[0].value, servantClass)
        outList.append(servant)
    
    return outList