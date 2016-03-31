import sqlite3

from services.Activite.Activite import Activite
from gestionBD import connection, deconnection


def allActivites():
    activitesTab = []

    connect = connection()
    curseur = connect.cursor()

    curseur.execute("select numero, nom from Activite")
    for row in curseur:
        activitesTab.append(Activite(row[0], row[1]).__dict__)

    connect.close()

    return activitesTab

def activite(activNom):
    activitesTab = []

    connect = connection()
    curseur = connect.cursor()
    curseur.execute("select numero, nom from Activite where nom LIKE ?", ["%"+activNom+"%"])

    for  row in curseur:
        activitesTab.append(Activite(row[0], row[1]).__dict__)

    connect.close()
    return activitesTab

'''

'''
