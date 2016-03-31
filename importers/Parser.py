from importers.Line import ActivityLine, EquipementLine, InstallationLine, EquipementActivite
"""
Classe qui récupère les données dans un fichier en fonction de son nom
"""

def parseRow(row,filename):
    if(filename=="csv/activites.csv"):
        numero = int(row[4].strip())
        nom = row[5].strip()
        return ActivityLine(numero, nom)
        
    elif(filename=="csv/equipements.csv"): 
        numero = int(row[4].strip())
        nom = row[5].strip()
        numero_installation = int(row[2].strip())
        return EquipementLine(numero, nom, numero_installation)
    
    elif(filename=="csv/installations.csv"):
        numero = int(row[1].strip())
        nom = row[0].strip()
        adresse = row[5].strip()+" "+row[6].strip()
        code_postal = row[4].strip() 
        ville = row[2].strip()
        latitude = row[10].strip()
        longitude = row[9].strip()
        return  InstallationLine(numero, nom, adresse, code_postal, ville, latitude, longitude)
        
    else:

        print("Erreur vos fichiers n'omt pas le bon nom")
        
def parseRow2(row):
    numero_equi = int(row[2].strip())
    numero_acti = int(row[4].strip())
    return EquipementActivite(numero_equi,numero_acti)

