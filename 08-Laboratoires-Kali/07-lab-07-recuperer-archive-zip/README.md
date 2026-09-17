---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 7
semaine_associee: 10
duree_minutes_indicative: 55
---

# Laboratoire 07 — Récupérer une archive ZIP pédagogique

## Mission et contexte

Créer une archive contenant un message inventé, passer la main au binôme, puis retrouver sa clé à partir de la liste d’exercice.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : zip, zip2john, John the Ripper, unzip.
- Mode : Manipulation hors ligne.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 55 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une archive chiffrée protège des octets avec un secret ; ce mécanisme diffère d’un hachage de mot de passe. Un extracteur comme zip2john produit une représentation que l’outil de recherche peut tester. La protection dépend aussi du format de chiffrement de l’archive.

<details>
<summary>Comprendre simplement</summary>
<p>On possède un coffre fermé et une copie de ses caractéristiques. On teste les clés sur cette copie sans demander à un serveur d’autoriser chaque essai.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
zip -j -P 'velo2026' travail/copies/lab07-coffre.zip travail/prive/message.txt
zip2john travail/copies/lab07-coffre.zip > travail/hashes/07-zip.txt
john --wordlist=travail/mots.txt --pot=travail/preuves/lab07.pot travail/hashes/07-zip.txt
john --show --pot=travail/preuves/lab07.pot travail/hashes/07-zip.txt
unzip -t travail/copies/lab07-coffre.zip
```

-j enlève les chemins internes ; -P place ici un mot de passe fictif dans la commande. Cette méthode expose le secret dans l’historique et n’est pas à employer pour des données réelles. unzip -t demande le secret et teste l’intégrité sans extraire les fichiers.

### 3. Interpréter

La clé trouvée permet le test d’intégrité. Le participant distingue le fichier ZIP, les données extraites pour John et le contenu déchiffré.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Décrire les limites du chiffrement traditionnel ZIP utilisé par zip -P et choisir une solution de chiffrement moderne pour un usage réel.

## Défi autonome

Un binôme remplace le secret par un autre élément de travail/mots.txt et documente le protocole d’échange sans partager de données personnelles.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Sur certaines installations Kali, appeler /usr/sbin/zip2john si la commande n’est pas trouvée.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab07`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Sur certaines installations Kali, appeler /usr/sbin/zip2john si la commande n’est pas trouvée.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [John the Ripper — Kali](https://www.kali.org/tools/john/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
