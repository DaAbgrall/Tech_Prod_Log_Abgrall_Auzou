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
    activesTab = []

    connect = connection()
    curseur = connect.cursor()
    query = "select numero, nom from Activite where nom = (?)"
    curseur.execute(query, (activNom))

    for  row in curseur:
        activitesTab.append(Activite(row[0], row[1]).__dict__)

    deconnection()
    for row in activitesTab:
        print(row[0]+ "  "+row[1])
    return activitesTab

'''

'''
