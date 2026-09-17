#!/usr/bin/env bash
# Prépare seulement le laboratoire 01 ; ne lance aucune recherche de mot de passe.
# Usage : bash preparer-lab01.sh [--verifier | --sans-installation]
set -euo pipefail

lab_mode="${1:-preparer}"
case "$lab_mode" in
  preparer|--verifier|--sans-installation) ;;
  --help)
    printf '%s\n' 'Usage : bash preparer-lab01.sh [--verifier | --sans-installation]'
    printf '%s\n' '--verifier : contrôles seuls, sans installation ni création de données.'
    printf '%s\n' '--sans-installation : crée les fichiers seulement si les outils sont présents.'
    exit 0 ;;
  *) printf '%s\n' 'Option inconnue. Utilisez --help.' >&2; exit 2 ;;
esac
if (( $# > 1 )); then
  printf '%s\n' 'Une seule option est acceptée.' >&2
  exit 2
fi
if ! grep -Eq '^ID="?kali"?$' /etc/os-release; then
  printf '%s\n' 'Ce préparateur est destiné à Kali Linux, pas à PowerShell.' >&2
  exit 1
fi

lab_script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
lab_base=$(cd -- "$lab_script_dir/.." && pwd -P)
if [[ ! -f "$lab_base/outils/preparer.py" ]]; then
  printf '%s\n' 'Conservez ce script dans le sous-dossier du laboratoire 01 du cours complet.' >&2
  exit 1
fi

lab_manquants=()
for lab_outil in python3 john md5sum gzip; do
  if ! command -v "$lab_outil" >/dev/null 2>&1; then
    lab_manquants+=("$lab_outil")
  fi
done
lab_source=''
if [[ -f /usr/share/wordlists/rockyou.txt.gz ]]; then
  lab_source=/usr/share/wordlists/rockyou.txt.gz
elif [[ -f /usr/share/wordlists/rockyou.txt ]]; then
  lab_source=/usr/share/wordlists/rockyou.txt
fi
if [[ -z "$lab_source" && ! -s "$lab_base/travail/rockyou.txt" ]]; then
  lab_manquants+=('RockYou (paquet wordlists)')
fi

if (( ${#lab_manquants[@]} )); then
  printf 'Éléments manquants : %s\n' "${lab_manquants[@]}"
  if [[ "$lab_mode" != preparer ]]; then
    printf '%s\n' 'Aucune installation ni création de données effectuée.' >&2
    exit 1
  fi
  printf '%s\n' 'Installation proposée : python3 john john-data wordlists gzip coreutils.'
  printf '%s\n' 'Elle nécessite Internet et une autorisation d’administration de cette Kali.'
  printf '%s\n' 'Si la machine est gérée par votre établissement, demandez à votre enseignant.'
  read -r -p 'Tapez OUI pour autoriser cette installation, ou Entrée pour arrêter : ' lab_accord || lab_accord=''
  if [[ "$lab_accord" != OUI ]]; then
    printf '%s\n' 'Installation refusée : aucun logiciel ni fichier de laboratoire modifié.'
    exit 1
  fi
  if (( EUID == 0 )); then
    apt-get update
    apt-get install python3 john john-data wordlists gzip coreutils
  else
    sudo apt-get update
    sudo apt-get install python3 john john-data wordlists gzip coreutils
  fi
  for lab_outil in python3 john md5sum gzip; do
    command -v "$lab_outil" >/dev/null 2>&1 || {
      printf 'Outil encore absent : %s\n' "$lab_outil" >&2
      exit 1
    }
  done
  if [[ -f /usr/share/wordlists/rockyou.txt.gz ]]; then
    lab_source=/usr/share/wordlists/rockyou.txt.gz
  elif [[ -f /usr/share/wordlists/rockyou.txt ]]; then
    lab_source=/usr/share/wordlists/rockyou.txt
  fi
fi

python3 - "$lab_base" "$lab_mode" "$lab_source" <<'PY'
import gzip
import hashlib
import os
import shutil
import sys
import tempfile
from pathlib import Path

base = Path(sys.argv[1])
verifier = sys.argv[2] == "--verifier"
source = Path(sys.argv[3]) if sys.argv[3] else None
travail = base / "travail"

def arreter(message):
    raise SystemExit("ARRÊT : " + message + " Aucun fichier existant n’a été remplacé.")

def dossier(chemin):
    if chemin.is_symlink():
        arreter(str(chemin) + " est un lien symbolique ; demandez de l’aide.")
    if chemin.exists():
        if not chemin.is_dir():
            arreter(str(chemin) + " n’est pas un dossier.")
    elif verifier:
        arreter(str(chemin) + " est absent.")
    else:
        chemin.mkdir()

def fichier(chemin, contenu):
    if chemin.is_symlink():
        arreter(str(chemin) + " est un lien symbolique.")
    if chemin.exists():
        if not chemin.is_file() or chemin.read_bytes() != contenu:
            arreter(str(chemin) + " diffère du matériel attendu ; conservez-le et demandez de l’aide.")
    elif verifier:
        arreter(str(chemin) + " est absent.")
    else:
        with chemin.open("xb") as sortie:
            sortie.write(contenu)

dossier(travail)
dossier(travail / "hashes")
dossier(travail / "preuves")
mot_fictif = b"password"
fichier(travail / "hashes/01-md5.txt",
        (hashlib.md5(mot_fictif).hexdigest() + "\n").encode("ascii"))
fichier(travail / "mots.txt",
        b"bonjour\npassword\nvelo2026\natelier\nboreal\nBoreal1\n0427\n")
origine = travail / "ORIGINE.md"
if not verifier and not origine.exists() and not origine.is_symlink():
    with origine.open("x", encoding="utf-8") as sortie:
        sortie.write("# Données fictives — laboratoire 01 seulement\n\n"
                     "Mot fictif : password. Aucun compte réel ne sert de cible.\n"
                     "Avant la préparation générale, conserver puis renommer ce dossier "
                     "selon le guide du cours ; ne pas supprimer les preuves.\n")

destination = travail / "rockyou.txt"
if destination.is_symlink():
    arreter("La copie RockYou est un lien symbolique.")
if destination.exists():
    if not destination.is_file() or destination.stat().st_size == 0:
        arreter("La copie RockYou est vide ou n’est pas un fichier.")
elif verifier:
    arreter("La copie RockYou manque.")
elif source is None or not source.is_file():
    arreter("RockYou manque dans le paquet wordlists.")
else:
    # Copie complète dans un fichier temporaire ; ne remplace jamais la destination.
    lab_temporaire = None
    try:
        with tempfile.NamedTemporaryFile(
                prefix=".rockyou-lab01-", dir=travail, delete=False) as sortie:
            lab_temporaire = Path(sortie.name)
            ouvrir = gzip.open if source.suffix == ".gz" else open
            with ouvrir(source, "rb") as entree:
                shutil.copyfileobj(entree, sortie)
        if lab_temporaire.stat().st_size == 0:
            arreter("La source RockYou est vide.")
        # Un lien physique publie la copie sans écraser un fichier apparu entre-temps.
        os.link(lab_temporaire, destination)
    finally:
        if lab_temporaire is not None:
            lab_temporaire.unlink(missing_ok=True)

with destination.open("rb") as entree:
    present = any(ligne.rstrip(b"\r\n") == mot_fictif for ligne in entree)
if not present:
    arreter("Le candidat pédagogique est absent de cette copie RockYou.")
print("PRÊT — empreinte, sept candidats, copie RockYou et dossier de preuves.")
print("Le mot fictif n’a pas été ajouté à RockYou ; sa présence a seulement été vérifiée.")
print("Aucune recherche John n’a été lancée et aucun mot de passe système n’a été changé.")
if not verifier:
    print("Ce script prépare seulement le laboratoire 01, pas les 49 autres.")
PY
