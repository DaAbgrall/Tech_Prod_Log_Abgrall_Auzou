"""
Fichier qui sert à creer des classes qui sont utilient pour l'insertion dans la base.
"""


class ActivityLine:
    def __init__(self, numero, nom):
        self.numero = numero
        self.nom = nom

    def __repr__(self):
        return "{} - {}".format(self.numero, self.nom)
        
class InstallationLine:
    def __init__(self, numero, nom, adresse, code_postal, ville, latitude, longitude):
        self.numero = numero
        self.nom = nom
        self.adresse = adresse
        self.code_postal = code_postal
        self.ville = ville
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "{} - {}".format(self.numero, self.nom, self.adresse, self.code_postal, self.ville, self.latitude, self.longitude)
        
        
class EquipementLine:
    def __init__(self, numero, nom, numero_installation):
        self.numero = numero
        self.nom = nom
        self.numero_installation = numero_installation
        
    def __repr__(self):
        return "{} - {}".format(self.numero, self.nom, self.numero_installation)
        
        
class EquipementActivite:
     def __init__(self, numero_equipement, numero_activite):
         self.numero_equipement = numero_equipement
         self.numero_activite = numero_activite
 
     def __repr__(self):
         return "{} - {}".format(self.numero_equipement, self.numero_activite)
        