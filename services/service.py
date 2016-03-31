import sqlite3

from services.Activite.Activite import Activite
from gestionBD import connection, deconnection


def service(ville, actvite):
    Tab = []

    connect = connection()
    curseur = connect.cursor()
    curseur.execute("SELECT i.numero, i.nom, e.numero, e.nom, a.numero, a.nom FROM installations i JOIN Equipement e ON i.numero = e.numero_installation JOIN Equipement_Activite ea ON e.numero = ea.numero_equipement JOIN Activite a ON ea.numero_activite = a.numero WHERE i.ville = "+ville+" AND a.nom LIKE "'%'actvite'l%'")

    for row in curseur:
        Tab.append(row)

    connect.close()
    return Tab

