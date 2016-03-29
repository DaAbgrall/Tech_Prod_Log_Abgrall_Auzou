import csv

import importers.Line 
from importers.Parser import parseRow, parseRow2
from importers.Creator import *

def importe(filename):
    importedActivities = []
    importedEquipement = []
    importedIntsallations = []
    i=0
    with open(filename, 'rt') as csvfile:
        activitiesReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        try:
            if(filename=="csv/activites.csv"):
                for row in activitiesReader:
                    activityLine = parseRow(row,filename)
                    if activityLine.numero not in importedActivities:
                        insertActivity(activityLine)
                        importedActivities.append(activityLine.numero)
                    
            elif(filename=="csv/equipements.csv"):
                for row in activitiesReader:
                    equipementLine = parseRow(row,filename)
                    if equipementLine.numero not in importedEquipement:
                        insertEquipement(equipementLine)
                        importedEquipement.append(equipementLine.numero)
                    EquipementActivite = parseRow2(row)
                    insertEquip_Acti (EquipementActivite)
 
                              
            elif(filename=="csv/installations.csv"):
                for row in activitiesReader:
                    installationsLine = parseRow(row,filename)
                    if installationsLine.numero not in importedIntsallations:
                        insertInstallation(installationsLine)
                        importedIntsallations.append(installationsLine.numero)
                        
            else:
                print("Erreur vos fichiers n'ont pas le bon nom")
                    
        except ValueError:
            print("Problem with row {} : {}".format(activitiesReader.line_num, ','.join(row)))
    csvfile.close()