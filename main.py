import pandas as pd
from dateutil.relativedelta import relativedelta
from fonction_de_base import *

fileName = "data.xlsx"

def readExcel(fileName, id):
    #Ont récupère les 4 dernier du client
    df = pd.read_excel(fileName)
    df = df[df["ID"] == id]
    df = df[["ID", "Date", "Réduction"]]

    # Vérifie le format de date et les trie
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(["Date"])

    return df

def calcule(df):
    for i in range(2, len(df)):
        if (df["Réduction"].iloc[i] == "Aucune réduction" and
        df["Réduction"].iloc[i-1] == "Aucune réduction" and
        df["Réduction"].iloc[i-2] == "Aucune réduction"):
            df.loc[df.index[i], "Réduction"] = "Réductions"
    print(df)

dataFram = readExcel("data.xlsx", "Théa")
calcule(dataFram)
# print(dataFram)
