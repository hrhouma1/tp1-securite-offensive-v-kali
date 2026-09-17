---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 32
semaine_associee: 10
duree_minutes_indicative: 45
---

# Laboratoire 32 — Auditer les programmes SUID sans obtenir root

## Mission et contexte

Inventorier un petit périmètre de programmes locaux et expliquer pourquoi le mécanisme exige une analyse, sans essayer d’élever les privilèges.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : find, stat, id.
- Mode : Inventaire local en lecture seule.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

SUID (Set User ID, exécution avec l’identité du propriétaire) est un mécanisme de privilèges sur certains exécutables. Sa présence n’est pas en soi une vulnérabilité. La possibilité de modifier un programme privilégié ou ses entrées peut en revanche créer une frontière de confiance défaillante.

<details>
<summary>Comprendre simplement</summary>
<p>Un employé peut déléguer une tâche avec un badge spécial ; il faut contrôler qui peut modifier les instructions de cette tâche.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
id
find /usr/bin -maxdepth 1 -type f -perm -4000 -print 2>/dev/null | head -n 15
stat -c '%a %U %G %n' /usr/bin/passwd
```

Le test -perm -4000 recherche le bit SUID. La commande ne l’ajoute à aucun fichier. La sortie dépend de la distribution ; la présence de passwd et son mode doivent être observés, pas supposés.

### 3. Interpréter

Un inventaire limité et une explication d’un usage légitime sont fournis. Aucune session root n’est ouverte.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Rédiger trois vérifications : propriétaire attendu, absence d’écriture non autorisée, provenance du paquet. Ne pas supprimer un bit au hasard sur un outil système.

## Défi autonome

Dessiner le chemin de confiance entre utilisateur, exécutable et fichiers qu’il utilise, sans exécuter d’action privilégiée.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Une liste de noms trouvés ne constitue pas une preuve d’élévation de privilèges.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab32`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Une liste de noms trouvés ne constitue pas une preuve d’élévation de privilèges.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [GNU Coreutils — permissions](https://www.gnu.org/software/coreutils/manual/html_node/File-permissions.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
