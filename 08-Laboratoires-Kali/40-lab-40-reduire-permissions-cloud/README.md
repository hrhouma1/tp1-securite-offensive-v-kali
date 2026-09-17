---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 40
semaine_associee: 12
duree_minutes_indicative: 50
---

# Laboratoire 40 — Réduire les permissions d’une politique cloud

## Mission et contexte

Examiner une politique de stockage fictive et proposer un accès limité à la lecture d’objets d’un périmètre donné.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3, éditeur.
- Mode : Analyse de politique simulée — aucun compte cloud.
- Lire la [théorie associée à la semaine 12](../../02-Semaines/Semaine-12-Securite-cloud-mobile-et-objets-connectes/01-Cours/Securite-du-cloud-du-mobile-et-des-objets-connectes.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 50 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

IAM (Identity and Access Management, gestion des identités et des accès) encadre les actions autorisées. Une politique très large peut permettre plus que le besoin métier. La forme d’un document seule ne démontre pas son effet complet : d’autres politiques et conditions peuvent intervenir.

<details>
<summary>Comprendre simplement</summary>
<p>Un badge permettant toutes les salles dépasse le besoin d’une personne chargée de lire un seul classeur.</p>
</details>

## Vocabulaire utile

- JSON (JavaScript Object Notation, notation structurée de données).

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
python3 -m json.tool travail/iam.json
cp travail/iam.json travail/copies/lab40-iam.json
python3 - <<'PY'
import json
from pathlib import Path
politique = json.loads(Path("travail/iam.json").read_text())
for regle in politique["Statement"]:
    print(regle["Effect"], regle["Action"], regle["Resource"])
PY
```

Le fichier utilise la forme générale d’une politique AWS (Amazon Web Services, services infonuagiques Amazon). Aucune commande d’administration cloud n’est lancée.

### 3. Interpréter

s3:* et Resource=* sont identifiés comme larges dans le scénario, sans conclure qu’un compte réel est exposé.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Dans la copie, proposer s3:GetObject limité à arn:aws:s3:::boreal-fictif/rapports/* et préciser que ce nom est fictif. Vérifier que le document reste du JSON valide.

## Défi autonome

Distinguer le besoin de lister les objets du besoin de lire un objet connu ; documenter une permission supplémentaire seulement si nécessaire.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>ARN (Amazon Resource Name, nom de ressource Amazon) identifie une ressource ; les permissions de liste d’un compartiment et de lecture d’un objet ne portent pas nécessairement sur la même ressource.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab40`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

ARN (Amazon Resource Name, nom de ressource Amazon) identifie une ressource ; les permissions de liste d’un compartiment et de lecture d’un objet ne portent pas nécessairement sur la même ressource.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [AWS — politiques et permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
