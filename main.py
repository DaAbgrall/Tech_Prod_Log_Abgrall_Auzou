import lecture
import gestionBD
import admin

def main ():
    creationBD
    test=lecture.recuperation('csv/23440003400026_J335_installations_table.csv')
    testco=gestionBD.connection
    cur=gestionBD.curseur
    cur.execution("SELECT SQLITE_VERSION()")
    print("test")
    testco.deconnection
