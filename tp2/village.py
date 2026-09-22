from habitants import Habitant

class Village:
    def __init__(self, nom):
        self.__nom = nom
        self.__habitants = []
    
    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        hab = Habitant(nom,age,adresse,animaux)
        self.__habitants.append(hab)
