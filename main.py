import lecture
import gestionBD

def main ():
    test=lecture.recuperation('csv/23440003400026_J335_installations_table.csv')
    testco=gestionBD.connection
    cur=gestionBD.curseur
    cur.execution("SELECT SQLITE_VERSION()")
    print("test")
    testco.deconnection
