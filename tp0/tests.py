import unittest
from tuples import recalibrer
from ensembles import robots_double_mission, ajouter_robot_mission

class TestJournalDeBord(unittest.TestCase):
    """Tests pour les fonctions sur les relevés (tuples)."""
    def test_recalibrer_capteur_existant(self):
        releve1 = ("laser_avant", 2.35, "m")
        releve2 = ("laser_arriere", 1.10, "m")
        releve3 = ("gyroscope", 87.5, "deg")
        releves = [releve1, releve2, releve3]
        nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

        self.assertEqual(len(nouveaux_releves),3)
        self.assertEqual(nouveaux_releves[0][0],"laser_avant")

    def test_recalibrer_capteur_absent(self):
        """Cas limite : le capteur demande n’existe pas."""
        releve1 = ("laser_avant", 2.35, "m")
        releve2 = ("laser_arriere", 1.10, "m")
        releve3 = ("gyroscope", 87.5, "deg")
        releves = [releve1, releve2, releve3]
        nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

        self.assertIn("laser_avant",nouveaux_releves[0])
    
class TestFlotteRobots(unittest.TestCase):
    """Tests pour les fonctions sur les relevés (tuples)."""
    def test_robot_double_mission(self):
        robots_exploration = {"R2", "R5", "R7"}
        robots_transport = {"R5", "R9", "R7", "R3"}

        double_mission = robots_double_mission(robots_exploration, robots_transport)
        self.assertEqual(double_mission,{"R5","R7"})        

    def test_ajouter_robot_mission(self):
        """Cas limite : le capteur demande n’existe pas."""
        robots_exploration = {"R2", "R5", "R7"}
        robots_transport = {"R5", "R9", "R7", "R3"}

        ajout = ajouter_robot_mission(robots_exploration, "R8")
        self.assertEqual(ajout,{"R5","R7","R8"})
        

        
if __name__ == "__main__":
    unittest.main(verbosity=2)