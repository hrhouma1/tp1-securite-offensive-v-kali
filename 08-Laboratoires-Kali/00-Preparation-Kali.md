---
tags: [cours, kali, preparation]
maj: 2026-09-17
statut: proposition-pedagogique
---

# Préparer les laboratoires sur Kali

## 1. Définir le périmètre

Utiliser uniquement une machine Kali de laboratoire autorisée. Les expériences visent des données fictives et `127.0.0.1`, l’adresse de boucle locale. Les domaines `.example` et les adresses du fichier de zone sont des données documentaires, pas des cibles à contacter. Aucun compte réel, site public, réseau voisin ou appareil tiers ne doit être testé.

Copier **le dossier complet du cours** dans le dossier personnel Linux de Kali, puis ouvrir un terminal dans `08-Laboratoires-Kali`. Le serveur réutilise `04-Ressources/Atelier-Boreal/atelier_boreal.py` : conserver cette arborescence.

Sous WSL (Windows Subsystem for Linux, sous-système Windows pour Linux), ne pas réaliser les exercices de permissions dans `/mnt/c` ; les droits d’un volume Windows ne reproduisent pas forcément les droits Linux. Burp demande une interface graphique Kali. Créer un instantané de la machine virtuelle si l’environnement le permet.

## 2. Installer les outils dans Kali

Une installation minimale ne contient pas forcément les outils. Les commandes suivantes nécessitent Internet, de l’espace disponible et l’autorisation d’administrer cette machine. Elles se lancent dans **Kali, pas dans PowerShell**. Aucune installation n’est faite automatiquement par le préparateur.

```bash
sudo apt update
sudo apt install python3 john john-data wordlists hashcat crunch cewl hydra nmap curl tcpdump tshark zip unzip gnupg openssl acl mosquitto mosquitto-clients
```

Seulement pour les ateliers 28 et 47 :

```bash
sudo apt install burpsuite metasploit-framework
```

Conserver la politique de l’établissement pour les droits de capture Wireshark. L’atelier capture avec `sudo tcpdump` et n’exige pas d’accorder ces droits à tous les utilisateurs. Mosquitto peut créer un service système : notre courtier d’exercice emploie le port local **18883**, distinct du port standard. Ne pas modifier un service préexistant.

```bash
python3 --version
for outil in john hashcat crunch cewl hydra nmap curl tcpdump tshark zip unzip gpg openssl setfacl getfacl mosquitto mosquitto_pub mosquitto_sub; do
  command -v "$outil" || printf 'Absent : %s\n' "$outil"
done
```

Le premier atelier utilise John the Ripper sans dépendre d’un processeur graphique. Hashcat en génération de candidats ne demande pas le même dispositif qu’un calcul accéléré. Si un moteur de calcul manque pour le défi optionnel, garder la méthode John ; ne pas employer `--force`.

## 3. Créer les données fictives

Depuis `08-Laboratoires-Kali` :

```bash
pwd
test -f outils/preparer.py
python3 outils/preparer.py
python3 outils/tester_atelier.py
```

Le préparateur crée `travail/` : empreintes, listes, journaux, fichiers et configurations synthétiques. Il refuse d’écraser ce dossier. Les secrets sont volontairement faibles et présents dans le matériel de préparation ; la banque est **formative**, pas une épreuve à réponses secrètes.

Les tests créent leurs propres fichiers temporaires et un serveur sur un port éphémère de boucle locale, puis les ferment. Ils n’installent rien et ne remplacent pas les preuves de l’étudiant.

## 4. Préparer rockyou.txt

```bash
if [ -f /usr/share/wordlists/rockyou.txt.gz ]; then
  gzip -dc /usr/share/wordlists/rockyou.txt.gz > travail/rockyou.txt
elif [ -f /usr/share/wordlists/rockyou.txt ]; then
  cp /usr/share/wordlists/rockyou.txt travail/rockyou.txt
else
  printf '%s\n' 'Dictionnaire absent : vérifier le paquet wordlists.'
fi
test -s travail/rockyou.txt
wc -l travail/rockyou.txt
```

Cette copie conserve le paquet système. Ne pas publier le dictionnaire dans le dépôt. Il sert aux tests **hors ligne** ; Hydra utilise uniquement les sept candidats fictifs de `travail/mots.txt`. [Documentation Kali du paquet wordlists](https://www.kali.org/tools/wordlists/).

## 5. Démarrer l’application locale

Dans un terminal A, depuis le même dossier :

```bash
python3 outils/serveur.py
```

Dans un terminal B :

```bash
curl --noproxy '*' --max-time 3 http://127.0.0.1:8080/health
```

Le serveur doit annoncer l’état prêt. Il écoute exclusivement sur `127.0.0.1`. Ne pas utiliser d’écoute réseau, de tunnel public ou d’hébergement externe.

| Port | Usage |
|---:|---|
| 8080 | Serveur principal |
| 8081 | Second serveur de l’atelier 16 |
| 8082 | Proxy Burp de l’atelier 28 |
| 18883 | Courtier de messages de l’atelier 44 |
| 8443 | Serveur chiffré de l’atelier 45 |

Le formulaire utilise un compte fictif `etudiant`. Les factures conservent l’identité Alice **simulée** de l’atelier d’origine. Le cookie de démonstration est fixe : ce portail n’est pas une authentification de production. Les routes corrigées démontrent un contrôle précis, pas la sécurité complète d’une application.

## 6. Arrêter et recommencer sans perdre les preuves

Arrêter chaque programme au premier plan avec `Ctrl+C` dans son terminal. Vérifier ses ports avec `ss -lnt`. Ne pas tuer un processus inconnu.

Pour recommencer, conserver d’abord ses preuves, fermer les outils et renommer uniquement le dossier de travail vers un nom encore libre :

```bash
pwd
test -f travail/ORIGINE.md
test ! -e travail-seance-01
mv -n -- travail travail-seance-01
python3 outils/preparer.py
```

Choisir un autre numéro si la destination existe. Vérifier que le déplacement a eu lieu ; le préparateur n’écrase jamais un dossier existant. Les dossiers de travail, cookies, clés et résultats de mots de passe sont exclus de Git par le fichier local `.gitignore`. Ne jamais supprimer le dossier du cours pour réinitialiser une expérience.

## Dépannage

| Symptôme | Vérification |
|---|---|
| Commande absente | Vérifier le paquet et le chemin dans Kali. |
| Port occupé | Examiner `ss -lntp`, sans arrêter un service inconnu. |
| Connexion refusée | Contrôler le terminal du serveur et le port 8080. |
| Faux succès Hydra | Relire le critère d’échec et confirmer avec curl. |
| John connaît déjà la réponse | Utiliser `--show` ou un nouveau nom de fichier pot. |
| Droits inchangés | Utiliser le système de fichiers Linux, pas `/mnt/c`. |
| Capture vide | Lancer la capture sur `lo` avant la requête. |
| Burp indisponible | Prévoir un bureau Kali ; ne pas prétendre avoir exécuté l’interface graphique sur une installation terminal seule. |

Retour : [Catalogue](00-Index.md).
