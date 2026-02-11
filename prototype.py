from datetime import date
from fonction_de_base import *


def generer_base_test():
    # Donnée de base
    nb = 12
    data = []
    d = date(2025, 2, 1)

    # Création de ma base de test
    for _ in range(nb):
        data.append([16482535, d, False])
        if d.month == 12:
            d = date(d.year + 1, 1, 1)
        else:
            d = date(d.year, d.month + 1, 1)

    return data

def moins_de_3_mois(day1, day2):
    # d2 doit être >= d1
    if day2 < day1:
        return False

    # Calcul de l’écart en années et mois
    year_diff = day2.year - day1.year
    month_diff = day2.month - day1.month + year_diff * 12

    if month_diff > 3:
        return False
    elif month_diff < 3:
        return True
    else:  # month_diff == 3, vérifier le jour
        return day2.day <= day1.day

def proxy(id=16482535, days=date(2025,12,1)):
    tab = []

    # Incert le rendez vous du jours
    data.append([id, days, False])

    # Fait la liste des rendez vous du client où aucune réduction n'a été apliquée
    for i in range(len(data)):
        if data[i][0] == id and data[i][2] == False:
            tab.append(data[i])

    # Trie la liste
    tab = sorted(tab, key=lambda x: x[1])

    # Regarde si le rendez vous du jour est éligible à une réduction
    if len(tab)>=4:
        if tab[len(tab)-4][2] == False and moins_de_3_mois(tab[len(tab)-4][1], tab[len(tab)-1][1]):
            for i in range(len(tab)-1, len(tab)-5, -1):
                tab[i][2]=True
    return tab






data = generer_base_test()
pprint(proxy(id=16482535, days=date(2026,2,1)))
