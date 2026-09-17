"""Vérifications des exemples pédagogiques ; aucun appel réseau extérieur."""
import unittest
from atelier_boreal import catalogue, facture, echo, traiter

class VerificationAtelier(unittest.TestCase):
    def test_recherche_normale(self):
        for mode in (False, True):
            statut, resultat = catalogue("Casque", mode)
            self.assertEqual(statut, 200)
            self.assertEqual(resultat["produits"], [(1, "Casque", 60)])

    def test_injection_et_correction(self):
        entree = "' OR 1=1 --"
        self.assertEqual(len(catalogue(entree, False)[1]["produits"]), 3)
        self.assertEqual(catalogue(entree, True)[1]["produits"], [])

    def test_apostrophe_legitime_et_accent(self):
        self.assertEqual(catalogue("Gants d'été", False)[0], 400)
        self.assertEqual(catalogue("Gants d'été", True)[1]["produits"][0][1], "Gants d'été")
        self.assertEqual(catalogue("Vélo", True)[1]["produits"][0][1], "Vélo")

    def test_propriete_et_service_normal(self):
        self.assertEqual(facture("202", False)[0], 200)
        self.assertEqual(facture("202", True)[0], 403)
        self.assertEqual(facture("101", True)[0], 200)
        self.assertEqual(facture("999", True)[0], 404)

    def test_affichage(self):
        self.assertIn("<b>Été</b>", echo("<b>Été</b>", False))
        self.assertIn("&lt;b&gt;Été&lt;/b&gt;", echo("<b>Été</b>", True))

    def test_routes_et_encodage(self):
        self.assertEqual(traiter("/health")[0], 200)
        self.assertEqual(traiter("/absent")[0], 404)
        self.assertEqual(traiter("/catalogue-corrige?nom=V%C3%A9lo")[2]["produits"][0][1], "Vélo")

if __name__ == "__main__":
    unittest.main(verbosity=2)
