"""Crée uniquement des données fictives dans le dossier travail voisin.
Usage : python3 outils/preparer.py
Ne modifie aucun compte ni service de Kali ; ne remplace pas un dossier existant.
"""
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DEST = BASE / "travail"

def construire(dest):
    dest.mkdir(exist_ok=False)
    def texte(nom, contenu):
        cible = dest / nom
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_text(contenu, encoding="utf-8")
    def donnees(nom, contenu):
        texte(nom, json.dumps(contenu, ensure_ascii=False, indent=2) + "\n")
    for dossier in ("preuves", "hashes", "prive", "public", "copies"):
        (dest / dossier).mkdir()
    texte("hashes/01-md5.txt", hashlib.md5(b"password").hexdigest() + "\n")
    texte("hashes/04-code.txt", hashlib.md5(b"0427").hexdigest() + "\n")
    texte("hashes/05-regles.txt", hashlib.md5(b"Boreal1").hexdigest() + "\n")
    texte("hashes/03-contexte.txt", hashlib.sha256(b"atelier").hexdigest() + "\n")
    texte("mots.txt", "bonjour\npassword\nvelo2026\natelier\nboreal\nBoreal1\n0427\n")
    texte("bases.txt", "boreal\natelier\nvelo\n")
    texte("prive/strategie.txt", "FICTIF — Projet vélos cargo, budget pédagogique 1200 unités.\n")
    texte("prive/message.txt", "FICTIF — Le colis pédagogique contient trois casques.\n")
    texte("public/notice.txt", "FICTIF — Les ateliers ferment à 18 heures.\n")
    texte("page.html", '<html lang="fr"><title>Atelier Boréal fictif</title><h1>atelier boreal velo</h1><p>Contact fictif : accueil@boreal.example. Responsable : Alice Exemple.</p></html>\n')
    texte("courriel.eml", "From: Support fictif <aide@boreal-support.example>\nTo: alice@boreal.example\nSubject: Simulation : validation urgente\nDate: Mon, 14 Sep 2026 10:00:00 +0000\nMIME-Version: 1.0\nContent-Type: text/plain; charset=utf-8\nContent-Transfer-Encoding: 8bit\n\nScénario fictif : une demande vous presse de saisir un mot de passe sur https://boreal-support.example/validation. Ne pas ouvrir ce lien ; analyser le message comme du texte.\n")
    texte("zone.txt", "$ORIGIN boreal.example.\n$TTL 3600\n@ IN SOA ns.boreal.example. admin.boreal.example. (1 3600 600 86400 3600)\n@ IN NS ns.boreal.example.\nns IN A 192.0.2.10\nportail IN A 192.0.2.20\nfactures IN CNAME portail\n")
    donnees("mandat.json", {"fiction": True, "cibles_autorisees": ["127.0.0.1"], "ports": [8080, 8081, 8082, 8443, 18883], "interdits": ["réseau de classe", "Internet", "comptes réels", "données personnelles"], "arret": "Ctrl+C"})
    donnees("autorisations-windows.json", {"fiction": True, "objet": "rapport-fictif.txt", "proprietaire": "Comptabilite", "dacl": [{"identite": "Comptabilite", "droits": ["lecture", "ecriture"]}, {"identite": "ToutLeMonde", "droits": ["lecture", "ecriture"]}]})
    donnees("inventaire.json", [
        {"id": "F01", "actif": "portail local", "constat": "facture tierce accessible", "preuve": True, "exposition": "locale simulée", "impact": "confidentialité"},
        {"id": "F02", "actif": "bannière locale", "constat": "version annoncée ancienne", "preuve": False, "exposition": "locale simulée", "impact": "à confirmer"},
        {"id": "F03", "actif": "copie de rapport", "constat": "écriture accordée à tous", "preuve": True, "exposition": "fichier fictif", "impact": "intégrité"}])
    donnees("segments.json", {"fiction": True, "noeuds": ["poste", "web", "comptabilite", "sauvegarde"], "liaisons": [["poste", "web"], ["web", "comptabilite"], ["comptabilite", "sauvegarde"]], "politique_cible": [["poste", "web"], ["comptabilite", "sauvegarde"]]})
    evenements = [
        {"heure": "2026-09-14T10:00:00Z", "compte": "alice", "action": "connexion", "statut": "echec", "octets": 0},
        {"heure": "2026-09-14T10:00:01Z", "compte": "alice", "action": "connexion", "statut": "echec", "octets": 0},
        {"heure": "2026-09-14T10:00:02Z", "compte": "alice", "action": "connexion", "statut": "succes", "octets": 0},
        {"heure": "2026-09-14T10:02:00Z", "compte": "alice", "action": "export", "statut": "succes", "octets": 8000000},
        {"heure": "2026-09-14T10:03:00Z", "compte": "benoit", "action": "lecture", "statut": "succes", "octets": 2000}]
    texte("evenements.jsonl", "".join(json.dumps(e, ensure_ascii=False) + "\n" for e in evenements))
    donnees("iam.json", {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": ["s3:*"], "Resource": "*"}]})
    donnees("stockage.json", {"fiction": True, "bucket": "boreal-fictif", "public": True, "chiffrement": True, "journalisation": False, "donnees": "factures synthétiques"})
    texte("Dockerfile.exemple", 'FROM python:3.12-slim\nWORKDIR /app\nENV MOT_DE_PASSE=FAUX_SECRET_DE_COURS\nCOPY . /app\nCMD ["python", "app.py"]\n')
    texte("AndroidManifest.xml", '<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="example.boreal"><uses-permission android:name="android.permission.READ_CONTACTS"/><application android:debuggable="true" android:usesCleartextTraffic="true"><activity android:name=".Accueil" android:exported="true"/></application></manifest>\n')
    donnees("objet-connecte.json", {"fiction": True, "objet": "camera-demonstration", "mot_de_passe_usine": True, "mises_a_jour": False, "messages": [{"topic": "atelier/temperature", "valeur": 21}, {"topic": "atelier/config", "valeur": "FAUX_JETON_DE_COURS"}]})
    texte("mosquitto-local.conf", "listener 18883 127.0.0.1\nallow_anonymous true\npersistence false\n")
    texte("cron-exemple.txt", "# DOCUMENT FICTIF : ne jamais installer cette ligne\n* * * * * root /atelier-partage/sauvegarde.sh\n# Scénario : /atelier-partage/sauvegarde.sh est modifiable par les employés.\n")
    texte("code-a-auditer.txt", 'import subprocess\nimport hashlib\nFAUX_SECRET = "EXEMPLE_NON_UTILISABLE"\ndef diagnostic(nom):\n    return subprocess.run("echo " + nom, shell=True)\ndef empreinte(mot):\n    return hashlib.md5(mot.encode()).hexdigest()\n')
    texte("wifi-scenario.json", json.dumps({"fiction": True, "ssid": "Boreal-laboratoire", "securite": "WPA2-Personal", "wps": True, "phrase": "password", "capture_radio": False}, indent=2))
    texte("rapport-modele.md", "# Rapport de laboratoire\n\n## Périmètre et autorisation\n\n## Méthode et limites\n\n## Constat démontré\n\n## Preuves et empreintes\n\n## Impact dans le scénario\n\n## Correction\n\n## Contre-test\n\n## Conclusion\n")
    texte("ORIGINE.md", "# Données synthétiques\nTous les noms, comptes, mots de passe, événements et secrets sont inventés. Ce dossier ne contient aucune preuve d'une compromission réelle.\n")
    return dest

if __name__ == "__main__":
    if DEST.exists():
        raise SystemExit("Le dossier travail existe déjà : conservation intégrale. Pour recommencer, le renommer manuellement après avoir conservé ses preuves.")
    print("Données fictives créées :", construire(DEST))
