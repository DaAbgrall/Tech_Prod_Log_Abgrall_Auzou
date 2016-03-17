'''
Classe representant un objet Equipement
'''
class Equipement:
    def __init__(self, numero, nom, numero_installation):
        self.numero = numero
        self.nom = nom
        self.numero_installation

    def __repr__(self):
        return "{} - {} - {}".format(self.numero, self.nom, self.numero_installation)
