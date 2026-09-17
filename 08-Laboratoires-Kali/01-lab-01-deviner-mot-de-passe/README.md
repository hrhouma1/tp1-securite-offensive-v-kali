---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 1
semaine_associee: 10
duree_minutes_indicative: 45
---

# Laboratoire 01 — Votre première mission : retrouver le mot de passe

L’objectif est de vous faire retrouver un mot de passe fictif, puis de vérifier votre réponse en comparant son empreinte à celle fournie. Pour préparer l’exercice, j’ai choisi le mot `password` : le préparateur calcule son empreinte, l’enregistre dans `travail/hashes/01-md5.txt` et place ce mot parmi les sept possibilités de la petite liste `travail/mots.txt`. RockYou contient déjà ce mot : nous ne l’y ajoutons pas et nous ne modifions aucun mot de passe de votre machine Kali.

**Oui, je vous annonce volontairement la réponse pour cette première démonstration !** Votre objectif est de comprendre et de prouver comment l’outil la retrouve. Écrire simplement `password` dans votre compte rendu ne prouve pas que vous avez réalisé l’expérience.

Je vous prépare cette enquête pour l’entreprise fictive **Atelier Boréal**, et je vous guide une étape à la fois. Vous n’avez pas besoin de connaître tous les outils de Kali pour commencer.

> Vous travaillez uniquement sur les fichiers fictifs de cet exercice, dans votre Kali de laboratoire autorisée. Aucun compte réel, site Internet ou appareil tiers ne sera testé. Le mot trouvé ne sert à vous connecter nulle part.

**Durée indicative : 45 minutes**, une fois les outils et fichiers prêts. Le défi bonus est facultatif. Votre réussite repose sur votre compréhension et vos preuves, pas sur votre vitesse.

## À quoi cela sert-il dans la vraie vie ?

Voici deux **situations professionnelles illustratives**, pas des incidents attribués à une entreprise précise :

| Situation | Ce qu’une équipe cherche à vérifier | Ce que vous apprenez aujourd’hui |
|---|---|---|
| Une équipe remplace une ancienne application. | Avec un mandat et des comptes de test, peut-elle montrer que l’ancien stockage facilite les essais de mots courants ? | Comprendre pourquoi une empreinte ne garantit pas, à elle seule, un stockage sûr. |
| Une entreprise forme ses employés aux mots de passe. | Peut-elle démontrer le risque des mots prévisibles avec des données fictives, sans demander les mots personnels ? | Produire une preuve reproductible, puis expliquer une amélioration. |

<details>
<summary>Deux cas réels documentés : RockYou et LinkedIn</summary>

**RockYou — dossier présenté en 2012 par la FTC (Federal Trade Commission, agence fédérale américaine de protection des consommateurs).** L’agence explique que sa plainte reprochait notamment à RockYou de conserver des mots de passe en clair et décrit l’exposition de données de 32 millions d’utilisateurs. « En clair » signifie que les mots sont directement lisibles. **Lien avec votre exercice :** comprendre les conséquences d’un mauvais stockage ; notre fichier contient une empreinte et ne reproduit donc pas à l’identique ce stockage en clair. [Source officielle : explication de la FTC](https://www.ftc.gov/business-guidance/blog/2012/03/data-security-coppa-rockyou-hurricane).

**LinkedIn — vol de données en 2012, notification complémentaire le 25 mai 2016.** Dans cette notification, LinkedIn indique que des données volées en 2012, dont des empreintes de mots de passe, avaient été remises en circulation ; l’entreprise précise qu’il ne s’agissait pas d’une nouvelle intrusion et décrit l’invalidation de mots de passe concernés. **Lien avec votre exercice :** une fuite d’empreintes reste un incident sérieux ; elle ne devient pas sans risque simplement parce que les mots ne sont pas directement lisibles. [Source primaire : notification LinkedIn, pages 1 et 2, conservée par le procureur général de Californie](https://oag.ca.gov/system/files/2016.05.25%20Email%20Notification_Important%20information%20about%20your%20LinkedIn%20account_0.pdf).

Nous ne prétendons pas que ces deux incidents utilisaient le même format ou le même outil que notre laboratoire. Aucun fichier de comptes de victimes n’est fourni : vous travaillez sur une empreinte créée pour le cours. La liste de candidats fournie par Kali est utilisée uniquement pour cette comparaison locale, jamais pour essayer des comptes de personnes réelles.

</details>

## 1. Avant l’enquête : qu’est-ce que je vous prépare ?

La préparation, c’est simplement **mettre le matériel sur la table avant de commencer**.

**Un indice.** Je choisis un mot de passe fictif. L’ordinateur calcule à partir de ce mot une suite de lettres et de chiffres appelée une **empreinte**. Le fichier conserve cette empreinte ; la fiche vous annonce volontairement le mot fictif pour que vous puissiez comprendre et vérifier chaque étape.

**Une liste de possibilités.** Nous utiliserons d’abord sept mots d’essai, puis le fichier `rockyou.txt`, qui contient beaucoup plus de mots de passe candidats. Un **candidat** est simplement un mot que l’on veut essayer.

**Un outil pour faire les essais.** Il s’appelle **John the Ripper**. Il prend un mot de la liste, calcule son empreinte et la compare à celle de l’exercice.

> « Ce mot produit-il la même empreinte ? Non ? J’essaie le suivant. Oui ? J’ai trouvé une correspondance ! »

**Un dossier pour vos résultats.** Vous pourrez y conserver vos observations et vos captures d’écran.

| Votre matériel | Où le trouver | À quoi il sert |
|---|---|---|
| L’indice | `travail/hashes/01-md5.txt` | Contient l’empreinte du mot à retrouver. |
| La petite liste | `travail/mots.txt` | Permet de comprendre avec seulement sept possibilités. |
| La grande liste | `travail/rockyou.txt` | Permet de refaire la recherche avec RockYou. |
| Le carnet de preuves | `travail/preuves/` | Conserve vos résultats et vos explications. |

<details>
<summary>« Empreinte », « hachage », « dictionnaire » : expliquez-moi simplement</summary>

Une **empreinte** est un résultat calculé à partir d’un texte. L’opération qui la produit s’appelle le **hachage**. Avec la même fonction et exactement le même texte, vous retrouvez le même résultat.

Un **dictionnaire**, ici, est simplement une liste de mots à essayer. Ce n’est pas forcément un dictionnaire de français.

John ne lit pas un mot caché dans l’empreinte et ne la « déchiffre » pas. Il calcule des empreintes de candidats et cherche une correspondance. Si le bon mot est absent de la liste, cette recherche par liste seule ne le trouvera pas.

</details>

## 2. Prérequis : faites cette préparation avant de commencer

**Pour aujourd’hui, vous n’avez besoin ni d’un serveur, ni d’une deuxième machine, ni des outils des 49 autres laboratoires.** Une fois le matériel prêt, la recherche fonctionne hors ligne.

Avant toute commande, vérifiez ces trois conditions :

- Vous avez une **machine Kali Linux autorisée**, avec un terminal et un espace où vous pouvez écrire. Le script ci-dessous n’installe pas Kali : la machine doit déjà exister.
- Vous avez copié **le dossier complet du cours**, avec le script `preparer-lab01.sh`, dans votre dossier personnel Linux. Si vous avez seulement cette page, demandez-moi le dossier du cours.
- Si des logiciels manquent, vous disposez d’Internet et de l’autorisation de les installer. Sur une machine gérée par l’établissement, demandez-moi avant d’accepter une installation.

### A. Ouvrez le bon dossier

Dans le gestionnaire de fichiers de Kali, entrez dans `08-Laboratoires-Kali`, puis ouvrez un terminal à cet endroit. **Restez dans ce dossier**, pas dans le sous-dossier de la fiche.

Le terminal est la fenêtre dans laquelle vous écrivez les commandes. Tapez une commande, puis appuyez sur Entrée ; n’ajoutez pas de symbole `$` devant les lignes proposées.

Lancez Bash pour utiliser le même interpréteur de commandes que dans la fiche :

```bash
bash
```

Vérifiez votre position :

```bash
pwd
```

**Ce que vous devez voir :** un chemin se terminant par `/08-Laboratoires-Kali`. Son début dépend de l’endroit où vous avez copié le cours.

### B. Vérifiez si le matériel est déjà prêt

```bash
bash 01-lab-01-deviner-mot-de-passe/preparer-lab01.sh --verifier
```

**Cette commande ne crée pas de données et n’installe rien.** Elle vérifie les outils puis les fichiers. Si un outil manque, elle s’arrête et vous le signale ; vous pourrez relancer la vérification après la préparation.

- Si vous obtenez **`PRÊT — empreinte, sept candidats, copie RockYou et dossier de preuves.`**, passez directement à l’étape 3.
- Sinon, lisez le message, puis ouvrez le bloc ci-dessous. Un message d’échec est une information utile, pas une raison de supprimer vos fichiers.

<details>
<summary>Mes prérequis ne sont pas prêts : exécuter le script preparer-lab01.sh</summary>

Je vous fournis le [fichier preparer-lab01.sh](preparer-lab01.sh). L’extension `.sh` indique ici un fichier de commandes pour Bash. Vous n’avez pas à recopier tout son code : il est déjà dans le dossier du laboratoire.

**Voici ce qu’il fait :**

1. Vérifier que vous êtes dans Kali et que le dossier du cours est présent.
2. Si des outils manquent, proposer l’installation des seuls logiciels nécessaires à ce laboratoire. **Il attend votre accord explicite `OUI` avant de lancer l’installation.**
3. Créer, uniquement s’ils manquent, l’empreinte du mot fictif `password`, la petite liste de sept candidats et le dossier de preuves.
4. Copier ou décompresser RockYou depuis le paquet installé, sans modifier l’original ni ajouter notre mot dans cette liste.
5. Vérifier les données attendues et afficher le message `PRÊT`.

Il ne lance aucune recherche John, n’ouvre aucun serveur et ne change aucun mot de passe système. Les commandes d’installation, si vous les acceptez, modifient bien les logiciels de Kali ; ce n’est pas la même chose que créer les fichiers d’exercice.

**Exécutez ceci depuis `08-Laboratoires-Kali` :**

```bash
bash 01-lab-01-deviner-mot-de-passe/preparer-lab01.sh
```

Ne lancez pas tout le script avec `sudo`. S’il doit installer des logiciels, il demandera les droits au moment nécessaire. Quand Kali demande le mot de passe d’administration, les caractères peuvent rester invisibles pendant la saisie : ce mot ne sera jamais utilisé comme cible.

Si vous ne voulez autoriser **aucune installation**, utilisez plutôt :

```bash
bash 01-lab-01-deviner-mot-de-passe/preparer-lab01.sh --sans-installation
```

Cette option crée les fichiers uniquement si les outils et une source RockYou sont déjà disponibles, ou si votre copie RockYou existe déjà.

**Si un fichier existant diffère du matériel attendu, le script s’arrête sans le remplacer.** Conservez ce fichier et montrez-moi le message. Une copie RockYou vide ou inadaptée n’est pas effacée automatiquement. Une erreur peut laisser les nouveaux fichiers déjà créés ; ils seront conservés à la reprise.

**Code complet du fichier `preparer-lab01.sh` :**

```bash
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
```

Lorsque le script affiche `PRÊT`, relancez la vérification de l’étape B puis passez à l’étape 3. Le script vérifie la présence du candidat dans votre copie RockYou ; cela ne constitue pas une preuve que n’importe quelle copie existante serait identique au paquet d’origine.

</details>

### C. Retenez ce que vous venez de préparer

Vous avez maintenant **l’indice, les listes, l’outil et le carnet de preuves**. Le fichier de l’indice contient l’empreinte, pas le mot en clair ; le mot fictif est annoncé dans la fiche et présent parmi les candidats pour faciliter l’apprentissage.

Le script prépare **seulement le laboratoire 01**. Si vous aviez déjà utilisé le préparateur général, il conserve les fichiers compatibles et les autres données. Avant de passer ensuite aux autres laboratoires avec une préparation minimale, conservez vos preuves et suivez la [procédure de préparation générale](../00-Preparation-Kali.md), qui prévoit de renommer le dossier de travail existant avant de créer un environnement complet.

**Point de contrôle :** ne commencez pas la recherche tant que la vérification n’affiche pas `PRÊT`.

## 3. Examinez l’indice et comprenez l’empreinte

### A. Ouvrez le fichier mystère

```bash
cat travail/hashes/01-md5.txt
```

**Ce que vous devez voir :** une seule ligne de 32 caractères, faite de chiffres et de lettres entre `a` et `f`.

**Ce que cela signifie :** vous observez l’empreinte, pas le mot de passe. `cat` affiche le contenu du fichier ; il ne le modifie pas.

Dans notre exercice, la méthode de calcul est **MD5 (Message Digest 5, une fonction de hachage)**. Je vous indique ce format pour que vous n’ayez pas à le deviner. La longueur d’une empreinte, à elle seule, ne suffit pas à identifier sa méthode de calcul.

### B. Faites une expérience avec un mot connu

Le mot `bonjour` ci-dessous est un exemple pour comprendre le mécanisme, pas la réponse à votre enquête.

```bash
printf '%s' 'bonjour' | md5sum
```

**Ce que vous devez voir :** une empreinte suivie d’un tiret. Relancez la même commande : l’empreinte reste identique.

Changez maintenant uniquement la première lettre :

```bash
printf '%s' 'Bonjour' | md5sum
```

**Ce que vous devez voir :** une autre empreinte.

**Ce que cela signifie :** même un changement de majuscule change le texte donné au calcul. Les espaces et les retours à la ligne comptent aussi.

<details>
<summary>Que signifient les morceaux de cette commande ?</summary>

- `printf '%s' 'bonjour'` fournit exactement le mot, sans ajouter de retour à la ligne.
- Le symbole `|` transmet ce texte à la commande suivante.
- `md5sum` calcule son empreinte MD5 (Message Digest 5).
- Le tiret affiché à droite indique que le texte vient de l’entrée de la commande plutôt que d’un fichier nommé.

N’ajoutez pas de guillemets typographiques ni d’espace à l’intérieur du mot lorsque vous recopiez une commande.

</details>

**Question à votre voisin :** « Si John essaie un mot, qu’est-ce qu’il doit comparer pour savoir s’il a trouvé une correspondance ? »

## 4. Résolvez une première énigme avec sept possibilités

Commencez par regarder la petite liste :

```bash
cat travail/mots.txt
```

**Ce que vous devez voir :** sept mots d’essai, un par ligne. Nous savons que cette liste pédagogique contient le mot recherché ; votre travail consiste à démontrer lequel correspond.

Lancez maintenant la recherche :

```bash
john --format=raw-md5 --wordlist=travail/mots.txt --pot=travail/preuves/lab01-mini.pot travail/hashes/01-md5.txt
```

Cette ligne est longue, mais elle donne seulement quatre consignes à John :

| Partie de la commande | Traduction simple |
|---|---|
| `--format=raw-md5` | « L’indice est une empreinte MD5 (Message Digest 5) brute. » |
| `--wordlist=travail/mots.txt` | « Essaie les mots de cette petite liste. » |
| `--pot=travail/preuves/lab01-mini.pot` | « Garde tes découvertes dans ce fichier de résultats. » |
| `travail/hashes/01-md5.txt` | « Voici le fichier contenant l’empreinte à comparer. » |

**Ce que vous devez voir :** des messages sur l’empreinte chargée et la recherche. Leur présentation varie selon la version de John ; vous n’avez pas à comprendre tous les chiffres.

Pour lire clairement le résultat, utilisez :

```bash
john --show --format=raw-md5 --pot=travail/preuves/lab01-mini.pot travail/hashes/01-md5.txt
```

**Ce que vous cherchez :** un mot retrouvé et un bilan indiquant une empreinte résolue. Par exemple, la mention `1 password hash cracked, 0 left` signifie « une empreinte de mot de passe résolue, aucune restante ». Il s’agit d’un exemple de formulation, pas d’une capture obtenue sur votre poste.

**Première réussite : vous avez retrouvé une correspondance parmi les sept possibilités.** Notez le résultat réellement affiché, même si le mot a été annoncé au début : c’est la preuve de votre manipulation qui compte.

<details>
<summary>John dit « No password hashes left to crack »</summary>

Cela peut signifier que John connaît déjà la réponse dans le fichier de résultats indiqué par `--pot`. Utilisez `--show` avec le même fichier pour vérifier.

Une réponse déjà mémorisée n’est pas la preuve d’une nouvelle recherche. Pour refaire une expérience depuis le début, choisissez un nouveau nom de fichier de résultats, sans supprimer l’ancien. Utilisez ce même nouveau nom dans la recherche et dans l’affichage.

</details>

## 5. Recommencez avec RockYou

Cette fois, vous donnez à John une liste beaucoup plus grande. **Nous changeons aussi le fichier de résultats**, pour ne pas réutiliser la découverte de la petite liste.

```bash
john --format=raw-md5 --wordlist=travail/rockyou.txt --pot=travail/preuves/lab01-rockyou.pot travail/hashes/01-md5.txt
```

Puis affichez le résultat de cette recherche :

```bash
john --show --format=raw-md5 --pot=travail/preuves/lab01-rockyou.pot travail/hashes/01-md5.txt
```

**Ce que vous devez voir :** le même mot retrouvé avec la copie RockYou prévue pour ce cours. Si le résultat diffère, ne recopiez pas celui d’un camarade : vérifiez la liste, le fichier d’empreinte et le fichier de résultats avec moi.

**Ce que cela signifie :** John a trouvé une correspondance avec un candidat de cette liste. Il n’a interrogé aucun site ni essayé de se connecter à votre compte Kali.

Vous venez de réaliser une **recherche par dictionnaire hors ligne** : « par dictionnaire » signifie « à partir d’une liste » ; « hors ligne » signifie ici « en comparant des données locales, sans soumettre les essais à un service de connexion ».

## 6. Prouvez que votre réponse est correcte

Je vous demande maintenant une preuve indépendante de l’annonce de John.

Dans le même terminal, lancez :

```bash
read -r -p 'Recopiez le mot de passe fictif trouvé : ' mot_trouve
```

**Ce que vous devez voir :** une invitation à saisir votre réponse. Tapez uniquement le mot trouvé, puis Entrée. Il est conservé temporairement sous le nom `mot_trouve`. Utilisez seulement le mot fictif de l’exercice.

Calculez son empreinte :

```bash
printf '%s' "$mot_trouve" | md5sum
```

Puis réaffichez l’indice :

```bash
cat travail/hashes/01-md5.txt
```

**Ce que vous devez voir :** les mêmes 32 caractères dans les deux résultats. Ignorez le tiret ajouté par `md5sum` ; comparez toute l’empreinte, pas seulement son début.

**Ce que cela signifie :** votre mot produit bien l’empreinte fournie. Vous avez vérifié la correspondance sans dépendre uniquement du résultat annoncé par John.

Si les empreintes diffèrent, vérifiez la majuscule, les espaces et votre saisie. Recommencez la saisie ; ne modifiez pas l’indice pour le faire correspondre à votre réponse.

## 7. Expliquez votre découverte avec vos mots

Complétez ces phrases dans une courte note :

1. « Au départ, mon fichier contenait… »
2. « RockYou a servi à… »
3. « John a essayé de… »
4. « Je sais que mon mot correspond à l’indice parce que… »

Je veux aussi vous entendre expliquer cette limite : **« Ne rien trouver dans une liste ne prouve pas qu’un mot de passe est impossible à retrouver. »**

### Ce qu’une entreprise devrait retenir

Dans notre scénario, le mot est prévisible et la méthode de stockage permet de tester les candidats rapidement. Nous avons volontairement choisi une configuration faible pour comprendre le mécanisme.

Pour protéger un vrai service, il faut notamment des mots de passe longs et uniques, ainsi qu’un stockage utilisant une fonction spécialement conçue pour les mots de passe, avec un sel unique. **Nous proposons cette amélioration ; nous ne l’avons pas déployée dans ce laboratoire.**

<details>
<summary>Un « sel », ce n’est pas celui de la cuisine !</summary>

Un **sel** est une valeur aléatoire ajoutée au calcul de stockage de chaque mot de passe. Deux comptes qui choisissent le même mot peuvent ainsi avoir des résultats stockés différents. Ce sel n’a pas besoin d’être secret.

Il faut aussi une fonction adaptée, dont le calcul coûte suffisamment de temps et, selon la méthode, de mémoire. Ajouter seulement un sel à notre calcul rapide ne transforme pas cet exercice en stockage sûr.

Nous reviendrons sur ces notions dans le [laboratoire sur les sels](../06-lab-06-comprendre-sel-cryptographique/README.md) et le [laboratoire sur le coût du calcul](../09-lab-09-mesurer-cout-mot-de-passe/README.md). Aujourd’hui, retenez surtout pourquoi un mot prévisible et un stockage rapide rendent les essais faciles.

</details>

## 8. Défi bonus : et si le bon mot disparaissait de la liste ?

Ce défi se fait sur **une copie de la petite liste**, pour observer facilement un échec. Gardez le même terminal et terminez d’abord la vérification de l’étape 6.

<details>
<summary>Je suis prêt : afficher le défi guidé</summary>

Avant de lancer les commandes, écrivez votre prédiction.

Créez une copie sans le mot que vous venez de vérifier :

```bash
grep -Fvx -- "$mot_trouve" travail/mots.txt > travail/lab01-sans-candidat.txt
```

Cette commande conserve les lignes qui ne sont pas exactement le mot trouvé. Elle ne modifie pas la liste d’origine. Si vous avez déjà une copie personnelle portant ce nom, choisissez un autre nom pour ne pas l’écraser.

Comptez les lignes restantes :

```bash
wc -l travail/lab01-sans-candidat.txt
```

Vous devez en obtenir **six** avec le matériel fourni. Sinon, arrêtez-vous et vérifiez la saisie de votre réponse.

Créez un nouveau fichier de résultats vide, avec un nom unique :

```bash
pot_defi=$(mktemp travail/preuves/lab01-defi-XXXXXX.pot)
```

Le nom est conservé dans `pot_defi`. Cette précaution évite que John réutilise une ancienne découverte.

Lancez la recherche avec la liste raccourcie :

```bash
john --format=raw-md5 --wordlist=travail/lab01-sans-candidat.txt --pot="$pot_defi" travail/hashes/01-md5.txt
```

Consultez son résultat :

```bash
john --show --format=raw-md5 --pot="$pot_defi" travail/hashes/01-md5.txt
```

Résultat attendu : aucune correspondance retrouvée et une empreinte restante. Ici, nous savons que le bon candidat a été retiré. Ce résultat ne prouve pas que le mot serait introuvable avec une autre liste ou une autre méthode.

Cette expérience change la liste testée ; elle ne corrige pas le stockage du mot de passe.

</details>

## 9. Ce que vous me remettez

Dans `travail/preuves/`, conservez une courte note nommée `lab01-compte-rendu.md` et vos captures nommées avec le préfixe `lab01`.

Votre remise doit montrer :

1. Le fichier d’empreinte utilisé et la confirmation que vous avez travaillé uniquement sur les données du cours.
2. La commande de recherche avec RockYou et le résultat affiché par John.
3. Le recalcul qui donne la même empreinte.
4. Vos quatre phrases d’explication, une limite de la recherche et une amélioration de sécurité proposée.

Le défi bonus ajoute votre prédiction, les six candidats restants et le résultat sans correspondance. Le nombre de secondes écoulées ne donne pas de points supplémentaires.

Ne joignez pas toute la liste RockYou, un mot de passe personnel ou une donnée provenant d’un autre compte. Vos résultats fictifs restent dans l’espace de remise prévu par l’enseignant, pas dans un dépôt public.

## 10. Si quelque chose bloque

| Ce que vous observez | Ce que vous faites |
|---|---|
| `command not found` | Un outil manque. Revenez à la vérification des outils ; ne passez pas à l’étape suivante. |
| `No such file or directory` | Un fichier ou dossier est introuvable. Vérifiez votre position avec `pwd`, puis les fichiers de préparation. |
| « travail existe déjà » | Le programme protège vos données. Vérifiez leur présence sans supprimer le dossier. |
| `No password hashes loaded` | John n’a pas chargé l’empreinte. Vérifiez le bon fichier et le format indiqué ; demandez-moi avant de modifier l’indice. |
| `Unknown ciphertext format` | La version de John ne reconnaît pas le format demandé. Faites vérifier l’installation Kali. |
| `No password hashes left to crack` | Vérifiez avec `--show` si le fichier de résultats contient déjà la réponse. |
| Rien n’est retrouvé | Vérifiez les chemins et la liste ; l’absence de résultat doit être expliquée, pas remplacée par un résultat inventé. |
| L’empreinte recalculée est différente | Ressaisissez exactement le mot : majuscules et espaces comptent. |
| Le terminal ne vous rend pas la main | La recherche peut être encore active. Vous pouvez l’arrêter avec `Ctrl+C` et me montrer le message. |

## 11. Terminer sans perdre votre travail

Conservez vos preuves. Si une recherche est encore active, arrêtez-la avec `Ctrl+C`. Aucun serveur n’a été nécessaire et aucun compte système n’a été modifié par cet exercice.

Ne supprimez pas le dossier du cours pour recommencer. Utilisez de nouveaux noms de fichiers de résultats ou la [procédure de conservation et de reprise](../00-Preparation-Kali.md).

**Mission accomplie lorsque vous pouvez dire : « J’ai retrouvé une correspondance, je l’ai vérifiée et je sais expliquer la limite de ma recherche. »**

## Pour aller plus loin

Le numéro 01 désigne le premier laboratoire de la banque, pas la première semaine du calendrier. Le lien théorique est la [semaine 10 — identités et permissions](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md), à consulter en approfondissement : sa lecture intégrale n’est pas exigée pour commencer cette enquête.

- [John the Ripper : utilisation documentée par Kali](https://www.kali.org/tools/john/).
- [RockYou et les listes disponibles dans Kali](https://www.kali.org/tools/wordlists/).
- [Options de John et fichier de résultats](https://github.com/openwall/john/blob/bleeding-jumbo/doc/OPTIONS).
- [Cas réels documentés, distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Barème commun : méthode, preuve et explication](../00-Evaluation-et-progression.md).
- [Préparation générale, pour les autres laboratoires](../00-Preparation-Kali.md).
- [Retour au catalogue](../00-Index.md).
