class Habitant():
    """Classe Habitants"""
    def __init__(self, nom, age, adresse, animaux=None):
        """Constructeur"""
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        if animaux is None:
            self.__animaux = {}
        else:
            self.__animaux = animaux
    
    def get_nom(self):
        return self.__nom
    
    @property
    def age(self):
        return self.__age
    
    def get_adresse(self):
        return self.__adresse
    
    def get_animaux(self):
        return self.__animaux
    
    def set_nom(self,nom):
        self.__nom = nom
    
    @age.setter
    def age(self,age):
        if age < 0 or age > 130:
            raise ValueError("Age impossible")
        else:
            self.__age  = age
    
    def set_adresse(self,adresse):
        self.__adresse = adresse
    
    def set_animaux(self,animaux):
        self.__animaux = animaux

    def affichage_adresse(self):
        """Affiche l'adresse"""
        print(f"{self.get_nom()} habite à {self.get_adresse()}")

    def compte_animal(self, animal):
        """Renvoie le nombre d'un animal donné"""
        return self.__animaux.get(animal,0)

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.get_nom() == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"

h1.age = 26
assert h1.age == 26
try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass
