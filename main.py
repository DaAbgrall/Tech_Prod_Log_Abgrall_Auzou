import gestionBD
import importers.Importer 
import admin
import sqlite3 as lite
"""
Classe qui lance la création de la base de donnée et l'insertion de données
"""
def main ():

    admin.creationBD()
    print("Insertion des donnees dans Activites")
    importers.Importer.importe("csv/activites.csv")
    print("Import Activite termine")
    print("Insertion des donnees dans Equipements")
    importers.Importer.importe("csv/equipements.csv")
    print("Import Equipement termine")
    print("Insertion des donnees dans Installations")
    importers.Importer.importe("csv/installations.csv")
    print("Import intsallation termine")
    print("Imports termine avec succes")
    
    # connec = lite.connect('projet.db')
    # curs = connec.cursor()
    # for row2 in curs.execute('SELECT * FROM Equipement_Activite'):
    #     print(row2)
    # connec.commit()
    # connec.close()
