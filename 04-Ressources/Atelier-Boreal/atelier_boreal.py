"""Atelier pédagogique local. Données inventées ; aucune dépendance externe.
Démarrage : python atelier_boreal.py
Identité simulée fixe : Alice. Ce programme n'implémente pas une authentification.
"""
import html
import json
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit

PRODUITS = [(1, "Casque", 60), (2, "Vélo", 450), (3, "Gants d'été", 25)]
FACTURES = {
    "101": {"numero": "101", "proprietaire": "Alice", "montant": 60},
    "202": {"numero": "202", "proprietaire": "Benoît", "montant": 450},
}

def catalogue(saisie, corrige=False):
    connexion = sqlite3.connect(":memory:")
    try:
        connexion.execute("CREATE TABLE produits (id INTEGER, nom TEXT, prix INTEGER)")
        connexion.executemany("INSERT INTO produits VALUES (?, ?, ?)", PRODUITS)
        if corrige:
            lignes = connexion.execute(
                "SELECT id, nom, prix FROM produits WHERE nom = ?", (saisie,)
            ).fetchall()
        else:
            # Faiblesse volontaire, exclusivement sur les produits inventés en mémoire.
            lignes = connexion.execute(
                "SELECT id, nom, prix FROM produits WHERE nom = '" + saisie + "'"
            ).fetchall()
        return 200, {"produits": lignes}
    except sqlite3.Error:
        return 400, {"erreur": "Entrée non traitable dans cette démonstration"}
    finally:
        connexion.close()

def facture(numero, corrige=False):
    document = FACTURES.get(numero)
    if document is None:
        return 404, {"erreur": "Facture inexistante"}
    if corrige and document["proprietaire"] != "Alice":
        return 403, {"erreur": "Accès refusé à Alice"}
    return 200, {"identite_simulee": "Alice", "facture": document}

def echo(texte, corrige=False):
    contenu = html.escape(texte) if corrige else texte
    return "<!doctype html><html lang='fr'><meta charset='utf-8'><title>Atelier Boréal</title><h1>Affichage pédagogique</h1><p>" + contenu + "</p></html>"

def traiter(chemin):
    morceaux = urlsplit(chemin)
    parametres = parse_qs(morceaux.query, keep_blank_values=True)
    route = morceaux.path
    if route == "/health":
        return 200, "application/json", {"etat": "prêt", "identite_simulee": "Alice"}
    if route in ("/catalogue", "/catalogue-corrige"):
        statut, contenu = catalogue(parametres.get("nom", [""])[0], route.endswith("-corrige"))
        return statut, "application/json", contenu
    if route in ("/facture", "/facture-corrige"):
        statut, contenu = facture(parametres.get("id", [""])[0], route.endswith("-corrige"))
        return statut, "application/json", contenu
    if route in ("/echo", "/echo-corrige"):
        contenu = echo(parametres.get("texte", ["Bonjour"])[0], route.endswith("-corrige"))
        return 200, "text/html", contenu
    if route == "/":
        return 200, "text/html", "<!doctype html><html lang='fr'><meta charset='utf-8'><title>Atelier Boréal</title><h1>Atelier Boréal</h1><p>Données fictives. Identité simulée : Alice.</p><ul><li><a href='/catalogue?nom=Casque'>Catalogue</a></li><li><a href='/facture?id=101'>Facture propre</a></li><li><a href='/facture-corrige?id=202'>Facture tierce, contrôle corrigé</a></li><li><a href='/echo?texte=Bonjour'>Affichage</a></li></ul></html>"
    return 404, "application/json", {"erreur": "Route inexistante"}

class AtelierHandler(BaseHTTPRequestHandler):
    server_version = "AtelierBoreal/1.0"
    sys_version = ""
    def do_GET(self):
        if self.headers.get("Host", "").split(":")[0] not in ("127.0.0.1", "localhost"):
            self.send_error(403, "Hôte local requis")
            return
        if len(self.path) > 4096:
            self.send_error(414, "Requête trop longue")
            return
        statut, mime, contenu = traiter(self.path)
        if mime == "application/json":
            contenu = json.dumps(contenu, ensure_ascii=False, indent=2)
        corps = contenu.encode("utf-8")
        self.send_response(statut)
        self.send_header("Content-Type", mime + "; charset=utf-8")
        self.send_header("Content-Length", str(len(corps)))
        self.send_header("Cache-Control", "no-store")
        # Les balises inoffensives restent visibles ; les scripts ne s'exécutent pas.
        self.send_header("Content-Security-Policy", "default-src 'none'; base-uri 'none'; form-action 'none'")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(corps)

def main():
    serveur = HTTPServer(("127.0.0.1", 8000), AtelierHandler)
    print("Atelier Boréal : http://127.0.0.1:8000 ; arrêt avec Ctrl+C.", flush=True)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt de l'atelier.", flush=True)
    finally:
        serveur.server_close()

if __name__ == "__main__":
    main()
