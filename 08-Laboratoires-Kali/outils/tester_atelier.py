"""Tests automatiques locaux des mécanismes pédagogiques, sans outil offensif."""
import importlib.util
import json
import tempfile
import unittest
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

ICI = Path(__file__).resolve().parent
def charger(nom):
    spec = importlib.util.spec_from_file_location(nom, ICI / (nom + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class Tests(unittest.TestCase):
    def test_donnees_et_non_ecrasement(self):
        preparer = charger("preparer")
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "travail"
            preparer.construire(destination)
            self.assertEqual((destination / "hashes/01-md5.txt").read_text().strip(), "5f4dcc3b5aa765d61d8327deb882cf99")
            self.assertEqual(len(json.loads((destination / "inventaire.json").read_text(encoding="utf-8"))), 3)
            with self.assertRaises(FileExistsError):
                preparer.construire(destination)
    def test_catalogue(self):
        app = charger("serveur").boreal
        self.assertEqual(len(app.catalogue("' OR '1'='1")[1]["produits"]), 3)
        self.assertEqual(app.catalogue("' OR '1'='1", True)[1]["produits"], [])
    def test_facture(self):
        app = charger("serveur").boreal
        self.assertEqual(app.facture("202")[0], 200)
        self.assertEqual(app.facture("202", True)[0], 403)
        self.assertEqual(app.facture("101", True)[0], 200)
    def test_affichage(self):
        app = charger("serveur").boreal
        self.assertIn("<b>bonjour</b>", app.echo("<b>bonjour</b>"))
        self.assertIn("&lt;b&gt;bonjour&lt;/b&gt;", app.echo("<b>bonjour</b>", True))

    def test_routes_http_locales(self):
        app = charger("serveur")
        with tempfile.TemporaryDirectory() as tmp:
            app.BASE = Path(tmp)
            charger("preparer").construire(app.BASE / "travail")
            serveur = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
            fil = threading.Thread(target=serveur.serve_forever, daemon=True)
            fil.start()
            base = "http://127.0.0.1:" + str(serveur.server_port)
            client = urllib.request.build_opener(urllib.request.ProxyHandler({}))
            def requete(route, data=None, headers=None):
                req = urllib.request.Request(base + route, data=data, headers=headers or {})
                try:
                    reponse = client.open(req, timeout=3)
                except urllib.error.HTTPError as erreur:
                    reponse = erreur
                with reponse:
                    return reponse.status, reponse.read().decode(), reponse.headers
            try:
                self.assertEqual(requete("/health")[0], 200)
                self.assertEqual(requete("/health", headers={"Host": "example.com"})[0], 403)
                self.assertEqual(requete("/telecharger?fichier=../prive/strategie.txt")[0], 200)
                self.assertEqual(requete("/telecharger-corrige?fichier=../prive/strategie.txt")[0], 403)
                self.assertEqual(requete("/telecharger?fichier=../../serveur.py")[0], 403)
                self.assertEqual(requete("/session")[0], 401)
                bon = b"utilisateur=etudiant&motdepasse=velo2026"
                faux = b"utilisateur=etudiant&motdepasse=incorrect"
                self.assertEqual(requete("/connexion", faux)[0], 401)
                self.assertEqual(requete("/connexion", bon)[0], 200)
                self.assertEqual(requete("/session", headers={"Cookie": "atelier=" + app.JETON})[0], 200)
                self.assertEqual([requete("/connexion-limitee", faux)[0] for _ in range(4)], [401, 401, 401, 429])
            finally:
                serveur.shutdown()
                serveur.server_close()
                fil.join(timeout=3)

if __name__ == "__main__":
    unittest.main()
