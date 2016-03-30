import sqlite3

from Line import ActivityLine

insertQueryA = "INSERT INTO Activite(numero, nom) VALUES (?, ?)"
insertQueryI = "INSERT INTO Installation(numero, nom, adresse, code_postal, ville, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)"
insertQueryE = "INSERT INTO Equipement(numero, nom, numero_installation) VALUES (?, ?, ?)"



def insertActivity(activity):
    connec = sqlite3.connect('projet.db')
    curs = connec.cursor()
    curs.execute(insertQueryA, (activity.numero, activity.nom))
    connec.commit()
    connec.close()

def insertInstallation(installation):
    connec = sqlite3.connect('projet.db')
    curs = connec.cursor()
    curs.execute(insertQueryI, (installation.numero, installation.nom, installation.adresse, installation.code_postal, installation.ville, installation.latitude, installation.longitude))
    connec.commit()
    connec.close()

def insertEquipement(equipement):
    connec = sqlite3.connect('projet.db')
    curs = connec.cursor()
    curs.execute(insertQueryE, (equipement.numero, equipement.nom, equipement.numero_installation))
    connec.commit()
    connec.close()
    
# def insertEquip_Acti(Equip_Activ):
#     connec = sqlite3.connect('projet.db')
#     curs = connec.cursor()
#     insertQuery = "INSERT INTO equipement_activite(numero_equipement, numero_activite) VALUES (?, ?)"
#     curs.execute(insertQuery, (equipement.numero_equipement, equipement.numero_activite))
#     connec.commit()
#     connec.close()