import pandas as pd
from fonction_de_base import *

def readExcel(fileName, id):
    dataFram = pd.read_excel(fileName)
    dataFram = dataFram[dataFram["ID"] == id]
    return dataFram

dataFram = readExcel("data.xlsx", 74698)
print(dataFram)