---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 50
semaine_associee: 15
duree_minutes_indicative: 180
---

# Laboratoire 50 — Mission finale — auditer et sécuriser Atelier Boréal

## Mission et contexte

En équipe de deux, réaliser trois constats de familles différentes, vérifier leurs corrections et présenter les limites de l’audit.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Outils des ateliers précédents.
- Mode : Mission intégrée locale — proposition formative. Avoir terminé plusieurs ateliers des familles mots de passe, web et systèmes.
- Lire la [théorie associée à la semaine 15](../../02-Semaines/Semaine-15-Revision-et-integration/01-Cours/Revision-generale-et-integration-des-competences.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 180 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une mission combine cadrage, observation, validation, correction et restitution. La valeur du travail se mesure à la qualité des preuves et à la réduction des risques démontrée, pas au nombre de commandes exécutées. La couverture reste limitée au laboratoire fourni.

<details>
<summary>Comprendre simplement</summary>
<p>L’inspection finale vérifie le bâtiment, organise les réparations et contrôle les travaux, sans prétendre avoir inspecté toute la ville.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
python3 -m json.tool travail/mandat.json
curl --noproxy '*' --max-time 3 http://127.0.0.1:8080/health
python3 outils/tester_atelier.py
cp travail/rapport-modele.md travail/preuves/lab50-rapport-final.md
```

Ces commandes constituent le contrôle de départ, pas une solution complète. Choisir ensuite dans les ateliers autorisés un défaut de secret, un contrôle d’accès web et un problème de permissions ou de configuration.

### 3. Interpréter

Trois fiches de constat, une chronologie de travail, un tableau de priorités et une démonstration de contre-tests sont livrés.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Pour chaque constat, montrer que la version corrigée bloque le cas interdit tout en conservant l’usage légitime. Si la correction est seulement proposée sur un fichier de configuration, l’indiquer explicitement.

## Défi autonome

Faire une revue contradictoire de 15 minutes : un autre binôme tente de reproduire un constat uniquement à partir du rapport.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Répartir les rôles testeur et gardien du périmètre puis les inverser. Une preuve manquante doit être signalée, pas remplacée par une sortie inventée.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab50`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Répartir les rôles testeur et gardien du périmètre puis les inverser. Une preuve manquante doit être signalée, pas remplacée par une sortie inventée.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — guide de test web](https://owasp.org/www-project-web-security-testing-guide/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
