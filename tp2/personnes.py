from multipledispatch import dispatch
from abc import ABC, abstractmethod

class Habitant(ABC):
    """Classe Habitants"""
    def __init__(self, nom, prenom, age):
        """Constructeur"""
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom
    
    @property
    def age(self):
        return self.__age
    
    def set_nom(self,nom):
        self.__nom = nom
    
    def set_prenom(self,prenom):
        self.__prenom = prenom
    
    @age.setter
    def age(self,age):
        if age < 0 or age > 130:
            raise ValueError("Age impossible")
        else:
            self.__age  = age
    
    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        pass

class Adulte(Habitant):
    def __init__(self, nom, prenom, age):
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans")
        super().__init__(nom, prenom, age)

    def calcul_nombre_annee_avant_retraite(self):
        age_retraite = 62
        if self.age >= age_retraite:
            return "Déjà à la retraite"
        else:
            return age_retraite - self.age

class Enfant(Habitant):
    def __init__(self, nom, prenom, age):
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans")

        super().__init__(nom, prenom, age)
    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur: Un enfant ne peut pas calculer sa retraite"

@dispatch(object,str)
def set_info(habitant,nom):
    habitant._Habitant_nom = nom

@dispatch(object,str,int)
def set_info(habitant,nom,age):
    habitant._Habitant_nom = nom
    habitant._Habitant_age = age

adulte = Adulte("Dupont", "Marie", 35)
enfant = Enfant("Martin", "Lucas", 12)
assert isinstance(adulte, Habitant)
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()
try:
    Enfant("Nom", "Prénom", 25)
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass