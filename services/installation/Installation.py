'''
Classe representant un objet Installation
'''
class Installation:
    def __init__(self, numero, nom, adresse, code_postale, ville, latitude, longitude):
        self.numero = numero
        self.nom = nom
        self.adresse
        self.code_postale
        self.ville
        self.latitude
        self.longitude

    def __repr__(self):
        return "{} - {} - {} - {} - {} - {} - {}".format(self.numero, self.nom, self.adresse, self.code_postale, self.ville, self.latitude, self.longitude)
