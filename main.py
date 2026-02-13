import pandas as pd
from dateutil.relativedelta import relativedelta
from fonction_de_base import *

def readExcel(fileName, id):
    #Ont récupère les 4 dernier du client
    df = pd.read_excel(fileName)
    df = df[df["ID"] == id]
    df = df.tail(4)

    # Vérifie le format de date et les trie
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(["Date"])

    return df


def calcul(df):
    resultats = {}

    for id_val, group in df.groupby("ID"):
        # Si moin de 4 rendez vous, renvoi False et arrète
        if len(df) < 4:
            resultats[id_val] = False
            continue

        # Calcule si les 4 derniée rendez vous ont eu lieu dans une fentre de 3 mois ou moin
        resultats[id_val] = df["Date"].max() <= df["Date"].min() + relativedelta(months=3)
        print(resultats)

    return df

dataFram = readExcel("data.xlsx", 74698)
x = calcul(dataFram)
#print(dataFram)