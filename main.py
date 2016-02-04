import lecture
import gestionBD
import admin

def main ():
    admin.creationBD
    test=lecture.recuperation('csv/23440003400026_J335_installations_table.csv')
    testco=gestionBD.connection
    cur=gestionBD.curseur
    gestionBD.execution("SELECT SQLITE_VERSION()")
    print("test")
    testco.deconnection
