from datetime import date
from fonction_de_base import *


def generer_base_test():
    data = [[] for x in range(10)]
    d = date(2025,2,1)
    for i in range(10):
        data[i].append(16482535)
        data[i].append(d)
        data[i].append(False)
        d = date(d.year, d.month + 1, d.day)
    return data

def moins_de_3_mois(d1, d2):
    """
    Retourne True si d2 est dans les 3 mois maximum après d1.
    On compare les années, mois et jours.
    """
    # d2 doit être >= d1
    if d2 < d1:
        return False

    # Calcul de l’écart en années et mois
    year_diff = d2.year - d1.year
    month_diff = d2.month - d1.month + year_diff * 12

    if month_diff > 3:
        return False
    elif month_diff < 3:
        return True
    else:  # month_diff == 3, vérifier le jour
        return d2.day <= d1.day

def proxy(id=16482535, days=date(2025,12,1)):
    tab = []
    data.append([id, days, False])
    for i in range(len(data)):
        if data[i][0] == id and data[i][2] == False:
            tab.append(data[i])
    tab = sorted(tab, key=lambda x: x[1])
    if len(tab)>4:
        if tab[len(tab)-4][2] == False and moins_de_3_mois(tab[len(tab)-4][1], tab[len(tab)-1][1]):
            for i in range(len(tab)-1, len(tab)-5, -1):
                tab[i][2]=True
    return tab






data = generer_base_test()
pprint(proxy())
