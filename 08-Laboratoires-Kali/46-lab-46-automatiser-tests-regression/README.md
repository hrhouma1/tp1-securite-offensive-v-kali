---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 46
semaine_associee: 9
duree_minutes_indicative: 60
---

# Laboratoire 46 — Automatiser un contrôle de sécurité et sa régression

## Mission et contexte

Exécuter les tests fournis, identifier les garanties vérifiées et ajouter un cas manquant sur une copie.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3, unittest.
- Mode : Tests locaux automatiques.
- Lire la [théorie associée à la semaine 9](../../02-Semaines/Semaine-09-Automatisation-et-Metasploit/01-Cours/Automatisation-des-tests-et-Metasploit.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 60 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Un test de régression vérifie qu’un comportement attendu reste vrai après une modification. Il doit couvrir le refus d’un cas interdit et le fonctionnement d’un cas autorisé. Une suite verte ne prouve que les propriétés réellement testées.

<details>
<summary>Comprendre simplement</summary>
<p>Après avoir réparé une serrure, on vérifie que l’intrus ne passe plus et que le propriétaire peut toujours entrer.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
python3 outils/tester_atelier.py
cp outils/tester_atelier.py outils/tester_atelier_extension.py
# Éditer uniquement la copie pour ajouter un test sur une facture inexistante.
python3 outils/tester_atelier_extension.py
```

Les tests créent des données temporaires et un serveur sur un port éphémère de boucle locale, puis les ferment. Ils n’ont pas besoin du serveur 8080. La copie est placée à côté du script initial pour conserver ses imports relatifs.

### 3. Interpréter

Les tests existants passent et le nouveau cas vérifie une réponse 404 pour une facture absente.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Introduire sur une copie un résultat attendu incorrect, constater l’échec, puis rétablir le test justifié. Ne jamais modifier la production pour faire taire artificiellement un test.

## Défi autonome

Rédiger une liste de trois propriétés non couvertes : charge, session de production, système d’exploitation réel, par exemple.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Un test doit échouer pour une raison compréhensible lorsqu’on casse la propriété qu’il contrôle.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab46`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Un test doit échouer pour une raison compréhensible lorsqu’on casse la propriété qu’il contrôle.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Python — tests unitaires](https://docs.python.org/3/library/unittest.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
