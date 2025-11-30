
import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        t=Terrain()
        t.charger("terrains/t1.txt")
        hauteur=t.hauteur
        largeur=t.largeur
        nb_Vide=0
        nb_Entre=0
        nb_Client=0
        nb_Obs=0
        for l in range(largeur):
            for h in range(hauteur):
                if t[h][l] == Case.ENTREE :
                    nb_Entre +=1
                if t[h][l] == Case.CLIENT :
                    nb_Client +=1
                if t[h][l] == Case.VIDE :
                    nb_Vide +=1
                if t[h][l] == Case.OBSTACLE :
                    nb_Obs +=1
                    
        if (hauteur*largeur != (nb_Vide+nb_Entre+nb_Client+nb_Obs)) or (nb_Entre<=0) or (nb_Client<=0): self.fail()


    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

