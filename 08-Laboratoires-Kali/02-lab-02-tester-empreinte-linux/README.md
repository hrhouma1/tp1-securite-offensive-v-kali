---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 2
semaine_associee: 10
duree_minutes_indicative: 45
---

# Laboratoire 02 — Comprendre une empreinte de mot de passe Linux

## Mission et contexte

Un collègue crée une empreinte fictive de type Linux. Comparer sa structure à celle du laboratoire 1, puis retrouver sa valeur avec une petite liste.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : OpenSSL, John the Ripper.
- Mode : Manipulation hors ligne.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Le format sha512crypt associe un mot de passe, un sel et un calcul répété. SHA (Secure Hash Algorithm, algorithme de hachage sécurisé) désigne une famille de fonctions ; sha512crypt n’est pas une simple empreinte SHA-512 du mot de passe. Aucun fichier système n’est nécessaire pour cette démonstration.

<details>
<summary>Comprendre simplement</summary>
<p>Deux coffres peuvent contenir le même objet mais avoir chacun leur mécanisme de fermeture. Le sel évite que deux entrées identiques aient automatiquement la même empreinte stockée.</p>
</details>

## Vocabulaire utile

- SHA-512 (Secure Hash Algorithm 512, algorithme d’empreinte de 512 bits).

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
printf '%s\n' 'velo2026' | openssl passwd -6 -salt boreal -stdin > travail/hashes/02-linux.txt
john --format=sha512crypt --wordlist=travail/mots.txt --pot=travail/preuves/lab02.pot travail/hashes/02-linux.txt
john --show --format=sha512crypt --pot=travail/preuves/lab02.pot travail/hashes/02-linux.txt
```

openssl passwd -6 fabrique uniquement une donnée d’exercice. Le sel fixe boreal rend la démonstration reproductible ; ce n’est pas une pratique de production. Ne jamais substituer un fichier de mots de passe du système à la cible fournie.

### 3. Interpréter

L’empreinte commence par $6$ et contient le sel. John retrouve le mot de passe choisi pour la démonstration.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Créer une seconde empreinte avec -salt autreSel et montrer que le même candidat peut correspondre à deux chaînes différentes.

## Défi autonome

Faire créer l’empreinte par un binôme avec un autre élément de travail/mots.txt, sans annoncer lequel.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Une erreur « No password hashes loaded » demande de vérifier le format et le contenu, pas d’accéder à /etc/shadow.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab02`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Une erreur « No password hashes loaded » demande de vérifier le format et le contenu, pas d’accéder à /etc/shadow.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [John the Ripper — Kali](https://www.kali.org/tools/john/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
