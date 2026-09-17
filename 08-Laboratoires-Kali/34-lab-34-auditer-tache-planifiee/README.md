---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 34
semaine_associee: 10
duree_minutes_indicative: 40
---

# Laboratoire 34 — Détecter une tâche privilégiée dépendant d’un fichier modifiable

## Mission et contexte

Analyser une ligne cron fictive et proposer une correction de la chaîne de permissions.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : grep, éditeur.
- Mode : Analyse de configuration fictive.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 40 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une tâche planifiée peut exécuter un programme avec une identité plus privilégiée que les personnes autorisées à modifier ce programme. C’est la chaîne de confiance qui compte : script, dossier, dépendances et paramètres. Le laboratoire n’installe aucune tâche cron.

<details>
<summary>Comprendre simplement</summary>
<p>Si une personne peut réécrire la liste d’ordres suivie par le responsable, elle influence les actions du responsable sans posséder son badge.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
grep -n . travail/cron-exemple.txt
cp travail/cron-exemple.txt travail/copies/lab34-proposition.txt
id
```

Le fichier est un document commenté ; ne jamais le copier dans /etc/cron.d ni l’envoyer à crontab. id décrit seulement l’identité de la session actuelle.

### 3. Interpréter

L’utilisateur d’exécution, le script appelé et l’hypothèse de modification sont identifiés séparément.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Annoter la proposition : propriétaire privilégié du script, répertoire parent non modifiable par les employés, chemins contrôlés, privilèges limités au besoin réel.

## Défi autonome

Proposer un test de contrôle de droits qui ne lance pas la tâche et une procédure de retour arrière.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Corriger seulement le mode du script peut échouer si son dossier parent permet de le remplacer.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab34`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Corriger seulement le mode du script peut échouer si son dossier parent permet de le remplacer.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [GNU Coreutils — permissions](https://www.gnu.org/software/coreutils/manual/html_node/File-permissions.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
