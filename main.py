import gestionBD
import importers.Importer 
import admin
import sqlite3 as lite


def main ():
    #admin.creationBD()
    #print("Insertion des donnees dans Activites")
    #importers.Importer.importe("csv/activites.csv")
    #print("Import Activite termine")
    #print("Insertion des donnees dans Equipements")
    #importers.Importer.importe("csv/equipements.csv")
    #print("Import Equipement termine")
    #print("Insertion des donnees dans Installations")
    #importers.Importer.importe("csv/installations.csv")
    #print("Import intsallation termine")
    #print("Imports termine avec succes")
    
    connec = lite.connect('projet.db')
    curs = connec.cursor()
    for row in curs.execute('SELECT e.numero, a.numero FROM Equipement e, Activite a'):
        print (row)

    connec.commit()
    connec.close()
    
    