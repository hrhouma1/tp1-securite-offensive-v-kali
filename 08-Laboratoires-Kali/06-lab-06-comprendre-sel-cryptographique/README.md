---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 6
semaine_associee: 10
duree_minutes_indicative: 35
---

# Laboratoire 06 — Comparer deux sels pour un même mot de passe

## Mission et contexte

Montrer au responsable fictif pourquoi deux utilisateurs ayant le même mot de passe ne doivent pas partager la même empreinte stockée.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : OpenSSL, diff.
- Mode : Manipulation hors ligne.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 35 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Un sel est une valeur distincte ajoutée au traitement de chaque mot de passe. Il peut être stocké avec l’empreinte ; il n’est généralement pas un secret. Il limite notamment la réutilisation directe de calculs préalables entre entrées, sans empêcher les essais sur une entrée donnée.

<details>
<summary>Comprendre simplement</summary>
<p>Chaque livre reçoit une pagination différente : retrouver une page dans un exemplaire ne donne plus directement son numéro dans tous les autres.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
printf '%s\n' 'velo2026' | openssl passwd -6 -salt selAlice -stdin > travail/preuves/lab06-alice.txt
printf '%s\n' 'velo2026' | openssl passwd -6 -salt selBenoit -stdin > travail/preuves/lab06-benoit.txt
diff travail/preuves/lab06-alice.txt travail/preuves/lab06-benoit.txt
```

diff retourne normalement le code 1 lorsque les fichiers diffèrent : ce résultat n’est pas une panne. Les sels lisibles sont choisis uniquement pour la démonstration.

### 3. Interpréter

Les deux lignes diffèrent alors que le mot de passe fourni est identique.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Décrire une création de sel aléatoire unique gérée par une bibliothèque de stockage de mots de passe ; ne pas inventer son propre algorithme.

## Défi autonome

Recalculer avec le même sel et le même mot pour vérifier le caractère déterministe du traitement.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Identifier séparément le marqueur de format, le sel et la partie calculée.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab06`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Identifier séparément le marqueur de format, le sel et la partie calculée.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OpenSSL — génération d’empreintes](https://docs.openssl.org/master/man1/openssl-passwd/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
