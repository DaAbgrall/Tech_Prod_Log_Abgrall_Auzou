import csv

import importers.Line 
from importers.Parser import parseRow
from importers.Creator import *

def importActivities(filename):
    importedActivities = []
    importedEquipement = []
    importedIntsallations = []

    with open(filename, 'rt') as csvfile:
        activitiesReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in activitiesReader:
            try:
                if(filename=="csv/activites.csv"):
                    activityLine = parseRow(row,filename)
                    if activityLine.numero not in importedActivities:
                        insertActivity(activityLine)
                        importedActivities.append(activityLine.numero)
                        
                elif(filename=="csv/equipements.csv"):  
                    equipementLine = parseRow(row,filename)
                    if equipementLine.numero not in importedEquipement:
                        insertEquipement(equipementLine)
                        importedEquipement.append(equipementLine.numero)
                
                elif(filename=="csv/installations.csv"):
                    installationsLine = parseRow(row,filename)
                    if installationsLine.numero not in importedIntsallations:
                        insertInstallation(installationsLine)
                        importedIntsallations.append(installationsLine.numero)
                else:
                    print("Erreur vos fichiers n'omt pas le bon nom")
                    
                    
            except ValueError:
                print("Problem with row {} : {}".format(activitiesReader.line_num, ','.join(row)))
    csvfile.close()