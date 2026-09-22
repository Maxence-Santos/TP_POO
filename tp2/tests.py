import unittest
from habitants import Habitant
from village import Village
from personnes import Adulte, Enfant

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l’encapsulation."""
    def test_age_setter_valide(self):
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        h1.age = 20
        self.assertEqual(h1.age,20)
    def test_age_setter_invalide(self):
        """Cas limite : age negatif."""
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        try:
            h1.age = -20
            self.assertRaises(ValueError("Age impossible"))
        except ValueError:
            pass
           
    def test_compte_animal_valide(self):
        """Cas normal compte_animal"""
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        self.assertEqual(h1.compte_animal("vaches"),3)
    
    def test_compte_animal_invalide(self):
        """Cas limite compte_animal"""
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        self.assertEqual(h1.compte_animal("moutons"),0)

class TestVillage(unittest.TestCase):
    def test_ajout_agrégation_valide(self):
        pytown = Village("PyTown")
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        pytown.ajouter_habitant_agregation(h1)
        self.assertEqual(len(pytown.get_habitants()),1)
    
    def test_ajout_composition_invalide(self):
        pytown = Village("PyTown")
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        pytown.ajouter_habitant_agregation(h1)

        v2 = Village("V2")
        v2.ajouter_habitant_agregation(h1)
        self.assertEqual(pytown.get_habitants()[0],h1) and self.assertEqual(v2.get_habitants()[0],h1)

class TestHeritage(unittest.TestCase):
    def test_calcul_retraite(self):
        adulte = Adulte("Dupont", "Marie", 35, "Rue A")
        try:
            enfant = Enfant("Martin", "Lucas", 22, "Rue B")
            self.assertRaises(ValueError("Un enfant doit avoir moins de 18 ans"))
        except ValueError:
            enfant = Enfant("Martin", "Lucas", 12, "Rue B")
        self.assertEqual(adulte.calcul_nombre_annee_avant_retraite(),27)
        self.assertEqual(enfant.calcul_nombre_annee_avant_retraite(),"Erreur: Un enfant ne peut pas calculer sa retraite")
            

if __name__ == "__main__":
    unittest.main(verbosity=2)