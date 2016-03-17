import gestionBD
import importers.Importer 
import admin

def main ():
    admin.creationBD
    importers.Importer.importActivities("csv/activites.csv")
    importers.Importer.importActivities("csv/equipements.csv")
    importers.Importer.importActivities("csv/installations.csv")
    print("test")
    testco.deconnection
