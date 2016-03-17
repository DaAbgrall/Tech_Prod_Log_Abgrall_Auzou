import sqlite3

from services.activite.Activite import Activite
from gestionBD import connection, deconnection


def allActivites():
    activitesTab = []

    connection = connection()
    curseur = connection.cursor()

    curseur.execute("select numero, nom from Activite")
    for row in curseur:
        activitesTab.append(Activite(row[0], row[1]).__dict__)

    deconnection()

    return activitesTab

def activite(activNom):
    activesTab = []

    connection = connection()
    curseur = connection.cursor()
    query = "select numero, nom from Activite where nom = (?)"
    curseur.execute(query, (activNom))

    for  row in curseur:
        activitesTab.append(Activite(row[0], row[1]).__dict__)

    deconnection()

    return activitesTab

'''

'''
