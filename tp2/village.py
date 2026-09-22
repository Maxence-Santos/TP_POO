from habitants import Habitant

class Village:
    """Classe Village"""
    def __init__(self, nom):
        """Constructeur"""
        self.__nom = nom
        self.__habitants = []
    
    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        hab = Habitant(nom,age,adresse,animaux)
        self.__habitants.append(hab)

    def ajouter_habitant_agregation(self, habitant):
        self.__habitants.append(habitant)
    
    def afficher_habitants(self):
        for hab in self.__habitants:
            print(f"{self.__habitants.__nom}\n")
    
    def get_habitants(self):
        return self.__habitants

pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages
assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()

"""ajouter_habitant_composition illustre une relation de composition car le villageois est créé en même temps qu'il est ajouté. Il n'existe donc pas en-dehors du village.
ajouter_habitant_agregation illustre une relation d’agrégation car le villageois est créé avant d'être ajouté, il existe donc en-dehors du villagee"""
