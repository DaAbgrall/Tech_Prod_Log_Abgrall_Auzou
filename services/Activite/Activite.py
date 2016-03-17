'''
Classe représentant un objet Activites
'''
class Activite
    def __init__(self, numero, nom):
        self.numero = numero
        self.nom = nom
        
    def __repr__(self):
        return "{} - {}".format(self.numero, self.nom)