"""Extension locale de l'Atelier Boréal existant ; jamais accessible au réseau.
Démarrage depuis 08-Laboratoires-Kali : python3 outils/serveur.py
Aucune authentification de production. Données et jetons entièrement fictifs.
"""
import argparse
import html
import importlib.util
import json
import time
from http.server import ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from urllib.parse import parse_qs, urlsplit

BASE = Path(__file__).resolve().parents[1]
RACINE = BASE.parent
spec = importlib.util.spec_from_file_location("atelier_boreal", RACINE / "04-Ressources/Atelier-Boreal/atelier_boreal.py")
boreal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boreal)
VERROU = Lock()
ESSAIS = {}
JETON = "session-fictive-alice"
TAILLE_MAX = 4096

class Handler(boreal.AtelierHandler):
    server_version = "BorealLabs/1.0"
    def local(self):
        return self.client_address[0] == "127.0.0.1" and self.headers.get("Host", "").split(":")[0] in ("127.0.0.1", "localhost")
    def repondre(self, code, body, mime="application/json", entetes=None):
        if not isinstance(body, str):
            body = json.dumps(body, ensure_ascii=False)
        contenu = body.encode()
        self.send_response(code)
        for cle, valeur in {"Content-Type": mime + "; charset=utf-8", "Content-Length": str(len(contenu)), "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff", "Content-Security-Policy": "default-src 'none'; base-uri 'none'; form-action 'none'", **(entetes or {})}.items():
            self.send_header(cle, valeur)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(contenu)
    def do_HEAD(self):
        if not self.local():
            return self.repondre(403, {"erreur": "Local uniquement"})
        self.repondre(200, "", "text/html")
    def do_GET(self):
        if not self.local():
            return self.repondre(403, {"erreur": "Local uniquement"})
        if len(self.path) > TAILLE_MAX:
            return self.repondre(414, {"erreur": "Requête trop longue"})
        url = urlsplit(self.path)
        params = parse_qs(url.query)
        if url.path == "/contexte":
            return self.repondre(200, (BASE / "travail/page.html").read_text(encoding="utf-8"), "text/html")
        if url.path in ("/telecharger", "/telecharger-corrige"):
            racine = (BASE / "travail").resolve()
            public = racine / "public"
            nom = params.get("fichier", ["notice.txt"])[0]
            cible = (public / nom).resolve()
            # Même la version pédagogique vulnérable reste limitée aux données fictives.
            borne = public if url.path.endswith("-corrige") else racine
            if not cible.is_relative_to(borne) or not cible.is_file():
                return self.repondre(403, {"erreur": "Accès refusé"})
            return self.repondre(200, cible.read_text(encoding="utf-8"), "text/plain")
        if url.path == "/session":
            cookie = self.headers.get("Cookie", "")
            return self.repondre(200 if cookie == "atelier=" + JETON else 401,
                                  {"authentifie": cookie == "atelier=" + JETON, "simulation": True})
        return super().do_GET()
    def do_POST(self):
        if not self.local():
            return self.repondre(403, {"erreur": "Local uniquement"})
        try:
            longueur = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self.repondre(400, {"erreur": "Longueur invalide"})
        if not 0 <= longueur <= TAILLE_MAX:
            return self.repondre(413, {"erreur": "Corps trop grand"})
        valeurs = parse_qs(self.rfile.read(longueur).decode("utf-8", errors="replace"))
        route = urlsplit(self.path).path
        if route not in ("/connexion", "/connexion-limitee"):
            return self.repondre(404, {"erreur": "Route inexistante"})
        user = valeurs.get("utilisateur", [""])[0]
        secret = valeurs.get("motdepasse", [""])[0]
        if route.endswith("-limitee"):
            with VERROU:
                cle = self.client_address[0]  # Une seule machine ; pas de contournement par changement de nom.
                debut, compteur = ESSAIS.get(cle, (time.monotonic(), 0))
                if time.monotonic() - debut >= 60:
                    debut, compteur = time.monotonic(), 0
                if compteur >= 3:
                    return self.repondre(429, "Trop de tentatives", "text/plain", {"Retry-After": "60"})
                ESSAIS[cle] = (debut, compteur + 1)
        if user == "etudiant" and secret == "velo2026":
            return self.repondre(200, "Connexion autorisée — compte fictif", "text/plain",
                                  {"Set-Cookie": "atelier=" + JETON + "; HttpOnly; SameSite=Strict; Path=/"})
        return self.repondre(401, "Identifiants incorrects", "text/plain")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, choices=(8080, 8081), default=8080)
    args = parser.parse_args()
    if not (BASE / "travail/ORIGINE.md").is_file():
        raise SystemExit("Préparer les données avec python3 outils/preparer.py")
    serveur = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Atelier fictif : http://127.0.0.1:{args.port} ; arrêt Ctrl+C.", flush=True)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        serveur.server_close()

if __name__ == "__main__":
    main()
