---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 49
semaine_associee: 13
duree_minutes_indicative: 60
---

# Laboratoire 49 — Transformer une découverte en rapport exploitable

## Mission et contexte

Rédiger une fiche de constat sur un seul défaut démontré et un résumé compréhensible par une direction non technique.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Éditeur Markdown, sha256sum.
- Mode : Synthèse des preuves du laboratoire.
- Lire la [théorie associée à la semaine 13](../../02-Semaines/Semaine-13-Rapport-et-recommandations/01-Cours/Rapport-professionnel-et-plan-de-remediation.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 60 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Un rapport utile relie un constat à une preuve, un impact contextualisé et une correction vérifiable. Il distingue résultat obtenu, hypothèse et limite. Un mot de passe retrouvé n’a pas besoin d’être répété dans toutes les captures et tous les résumés.

<details>
<summary>Comprendre simplement</summary>
<p>Le client attend un diagnostic et une réparation contrôlable, pas le contenu brut de la boîte à outils.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
cp travail/rapport-modele.md travail/preuves/lab49-rapport.md
# Choisir une preuve textuelle réellement produite et calculer son empreinte.
sha256sum travail/rapport-modele.md
# Éditer travail/preuves/lab49-rapport.md avec les preuves de son propre atelier.
```

L’empreinte affichée par la commande porte sur le modèle, pas sur la preuve de votre constat. Remplacer le chemin par celui de la pièce réellement citée avant de constituer le dossier final.

### 3. Interpréter

Le rapport contient une preuve précise, une limite, une recommandation et un contre-test positif et négatif.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Faire relire le document par un binôme qui n’a pas participé au test ; corriger toute phrase qu’il ne peut relier à une pièce.

## Défi autonome

Présenter le constat en trois minutes, avec une seule diapositive ou une page et une action prioritaire.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Une capture sans commande, contexte ni résultat lisible ne suffit pas à rendre un constat reproductible.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab49`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Une capture sans commande, contexte ni résultat lisible ne suffit pas à rendre un constat reproductible.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — guide de test web](https://owasp.org/www-project-web-security-testing-guide/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
