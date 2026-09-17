---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 42
semaine_associee: 12
duree_minutes_indicative: 45
---

# Laboratoire 42 — Auditer une recette de conteneur sans l’exécuter

## Mission et contexte

Trouver trois pistes d’amélioration dans une recette fictive sans télécharger ni lancer d’image.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : grep, éditeur.
- Mode : Analyse statique — Docker non requis.
- Lire la [théorie associée à la semaine 12](../../02-Semaines/Semaine-12-Securite-cloud-mobile-et-objets-connectes/01-Cours/Securite-du-cloud-du-mobile-et-des-objets-connectes.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Un Dockerfile décrit la construction d’une image. Copier trop de fichiers, embarquer un secret et exécuter avec une identité inutilement privilégiée sont des sujets distincts. L’audit du texte ne vérifie pas les vulnérabilités présentes dans l’image ni ses conditions réelles d’exécution.

<details>
<summary>Comprendre simplement</summary>
<p>On inspecte une recette avant de construire le véhicule ; cela ne remplace pas son contrôle une fois assemblé.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
grep -n . travail/Dockerfile.exemple
cp travail/Dockerfile.exemple travail/copies/lab42-Dockerfile
grep -nE 'FROM|ENV|COPY|USER' travail/copies/lab42-Dockerfile
```

Le texte utilise un faux secret explicite. Le laboratoire n’exécute ni docker build ni docker run.

### 3. Interpréter

La copie documente secret embarqué, contexte copié trop largement et absence d’identité applicative explicite.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Proposer un contexte de copie limité, un secret fourni au moment de l’exécution et un utilisateur dédié ; expliquer les permissions nécessaires à l’application.

## Défi autonome

Rédiger un .dockerignore pédagogique dans travail/copies en excluant preuves, secrets et archives de travail.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Ajouter USER sans préparer les droits des fichiers peut casser le service : une correction doit être testable.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab42`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Ajouter USER sans préparer les droits des fichiers peut casser le service : une correction doit être testable.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Docker — pratiques de construction](https://docs.docker.com/build/building/best-practices/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
