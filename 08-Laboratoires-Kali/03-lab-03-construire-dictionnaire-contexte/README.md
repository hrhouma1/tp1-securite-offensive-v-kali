---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 3
semaine_associee: 3
duree_minutes_indicative: 45
---

# Laboratoire 03 — Construire un dictionnaire à partir d’un site fictif

## Mission et contexte

Le portail fictif parle de l’atelier et des vélos. Produire une petite liste contextuelle puis tester une empreinte synthétique, sans collecter de données sur des personnes réelles.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : CeWL, John the Ripper.
- Mode : Service local requis.
- Lire la [théorie associée à la semaine 3](../../02-Semaines/Semaine-03-Renseignement-sources-ouvertes/01-Cours/Renseignement-et-reconnaissance-passive.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

OSINT (Open Source Intelligence, renseignement de sources ouvertes) consiste à exploiter des informations accessibles dans un périmètre défini. Une liste contextuelle transforme des mots du site en hypothèses de test ; elle ne prouve pas qu’un employé emploie réellement ces mots.

<details>
<summary>Comprendre simplement</summary>
<p>On constitue un trousseau adapté au bâtiment, sans prétendre que chaque clé ouvre une porte.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
cewl -d 0 -m 4 -w travail/preuves/lab03-mots.txt http://127.0.0.1:8080/contexte
sort -u travail/preuves/lab03-mots.txt | head -n 20
john --format=raw-sha256 --wordlist=travail/preuves/lab03-mots.txt --pot=travail/preuves/lab03.pot travail/hashes/03-contexte.txt
john --show --format=raw-sha256 --pot=travail/preuves/lab03.pot travail/hashes/03-contexte.txt
```

-d 0 limite CeWL à la page initiale et -m 4 conserve les mots d’au moins quatre caractères. Le serveur ne propose aucun lien externe à suivre.

### 3. Interpréter

La liste contient du vocabulaire de la page. Une correspondance montre pourquoi un mot lié à l’organisation peut rester prévisible.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Expliquer pourquoi modifier le nom de l’entreprise dans un mot de passe n’est pas une stratégie suffisante. Proposer une phrase aléatoire indépendante du contexte.

## Défi autonome

Comparer le nombre de candidats de cette liste à rockyou.txt, puis discuter la couverture plutôt que la seule taille.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Vérifier que /contexte répond avant d’utiliser CeWL ; le serveur doit rester dans son propre terminal.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab03`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Vérifier que /contexte répond avant d’utiliser CeWL ; le serveur doit rester dans son propre terminal.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [CeWL — Kali](https://www.kali.org/tools/cewl/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
