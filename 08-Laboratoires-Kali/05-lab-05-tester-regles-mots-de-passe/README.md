---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 5
semaine_associee: 10
duree_minutes_indicative: 45
---

# Laboratoire 05 — Montrer les limites de la majuscule et du chiffre final

## Mission et contexte

Retrouver une empreinte fabriquée à partir d’un mot du scénario avec une transformation simple.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Hashcat, John the Ripper.
- Mode : Manipulation hors ligne.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une règle transforme des mots de base en variantes. Mettre une majuscule puis ajouter un chiffre crée une structure souvent prévisible. Une règle n’est pas un déchiffrement : elle élargit de façon contrôlée la liste de candidats.

<details>
<summary>Comprendre simplement</summary>
<p>Changer la couleur d’une clé ne crée pas forcément une serrure plus solide ; ici, la variation est attendue par le testeur.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
printf '%s\n' 'c$1' > travail/preuves/lab05.rule
hashcat --stdout travail/bases.txt -r travail/preuves/lab05.rule > travail/preuves/lab05-candidats.txt
john --format=raw-md5 --wordlist=travail/preuves/lab05-candidats.txt --pot=travail/preuves/lab05.pot travail/hashes/05-regles.txt
john --show --format=raw-md5 --pot=travail/preuves/lab05.pot travail/hashes/05-regles.txt
```

Dans la syntaxe des règles Hashcat, c capitalise et $1 ajoute le caractère 1. Les apostrophes autour de la règle empêchent le shell d’interpréter le dollar. --stdout génère des candidats sans lancer de calcul sur un processeur graphique.

### 3. Interpréter

Trois variantes sont produites ; l’une correspond à l’empreinte.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Proposer une règle organisationnelle qui ne se limite pas à « une majuscule et un chiffre ». Justifier le rôle de la longueur, de l’unicité et du stockage adapté.

## Défi autonome

Ajouter une deuxième règle bornée, compter les candidats uniques et expliquer pourquoi le compte brut peut comporter des doublons.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Lire les candidats avant de tester. Si le fichier est vide, corriger la génération avant de lancer John.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab05`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Lire les candidats avant de tester. Si le fichier est vide, corriger la génération avant de lancer John.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Hashcat — documentation des options](https://hashcat.net/wiki/doku.php?id=hashcat).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
