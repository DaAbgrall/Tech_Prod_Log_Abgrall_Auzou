import sqlite3

from Line import ActivityLine
import gestionBD

insertQueryA = "INSERT INTO Activite(numero, nom) VALUES (?, ?)"
insertQueryI = "INSERT INTO Installation(numero, nom, adresse, code_postal, ville, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)"
insertQueryE = "INSERT INTO Equipement(numero, nom, numero_installation) VALUES (?, ?, ?)"
insertQueryE_A = "INSERT INTO equipement_activite(numero_equipement, numero_activite) VALUES (?, ?)"



def insertActivity(activity):
    connec = sqlite3.connect('projet.db')
    curs = connec.cursor()
    curs.execute(insertQueryA, (activity.numero, activity.nom))
    gestionBD.deconnection

def insertInstallation(installation):
    connec = sqlite3.connect('projet.db')
    curs = connec.cursor()
    curs.execute(insertQueryI, (installation.numero, installation.nom, installation.adresse, installation.code_postal, installation.ville, installation.latitude, installation.longitude))
    gestionBD.deconnection

def insertEquipement(equipement):
    connec = sqlite3.connect('projet.db')
    curs = connec.cursor()
    insertQuery = "INSERT INTO Equipement(numero, nom, numero_installation) VALUES (?, ?, ?)"
    curs.execute(insertQueryE, (equipement.numero, equipement.nom, equipement.numero_installation))
    gestionBD.deconnection
    
def insertEquip_Acti(Equip_Activ):
    connec = sqlite3.connect('projet.db')
    curs = connec.cursor()
    curs.execute(insertQueryE_A, (Equip_Activ.numero_equipement, Equip_Activ.numero_activite))
    gestionBD.deconnection
     
