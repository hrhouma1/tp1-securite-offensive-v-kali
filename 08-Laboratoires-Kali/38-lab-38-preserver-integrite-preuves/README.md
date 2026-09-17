---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 38
semaine_associee: 13
duree_minutes_indicative: 40
---

# Laboratoire 38 — Détecter une modification de preuve

## Mission et contexte

Conserver un original fictif, modifier uniquement une copie et prouver la différence.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : sha256sum, cp, cmp.
- Mode : Fichiers fictifs uniquement.
- Lire la [théorie associée à la semaine 13](../../02-Semaines/Semaine-13-Rapport-et-recommandations/01-Cours/Rapport-professionnel-et-plan-de-remediation.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 40 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une empreinte permet de comparer des octets ; elle ne prouve pas à elle seule la provenance ou la véracité d’un document. SHA-256 (Secure Hash Algorithm sur 256 bits, algorithme d’empreinte de 256 bits) aide à détecter une modification entre deux vérifications.

<details>
<summary>Comprendre simplement</summary>
<p>Un scellé peut révéler qu’un paquet a changé, sans certifier que son contenu initial racontait la vérité.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
cp travail/evenements.jsonl travail/copies/lab38-traces.jsonl
sha256sum travail/evenements.jsonl travail/copies/lab38-traces.jsonl
printf '\n' >> travail/copies/lab38-traces.jsonl
sha256sum travail/evenements.jsonl travail/copies/lab38-traces.jsonl
cmp travail/evenements.jsonl travail/copies/lab38-traces.jsonl
```

Le seul ajout est un retour à la ligne dans la copie. cmp signale normalement une différence ; son code non nul n’est pas une panne de l’atelier.

### 3. Interpréter

Les empreintes sont d’abord égales puis différentes, tandis que l’original reste inchangé.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Rédiger une fiche de collecte avec origine fictive, date de collecte réelle, outil, empreinte et distinction original/copie.

## Défi autonome

Expliquer pourquoi une empreinte publiée au même endroit qu’un fichier modifiable n’assure pas seule une chaîne de confiance.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Ne pas « corriger » l’original pour le faire correspondre à la copie.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab38`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Ne pas « corriger » l’original pour le faire correspondre à la copie.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Python — fonctions d’empreinte et de dérivation](https://docs.python.org/3/library/hashlib.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
