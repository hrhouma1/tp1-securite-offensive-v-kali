---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 29
semaine_associee: 14
duree_minutes_indicative: 45
---

# Laboratoire 29 — Repérer une injection de commandes avant exécution

## Mission et contexte

Identifier dans le texte de code fourni un usage risqué du shell, puis proposer une alternative sans lancer le programme analysé.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3, ast.
- Mode : Analyse statique — fichier fourni non exécuté.
- Lire la [théorie associée à la semaine 14](../../02-Semaines/Semaine-14-Analyse-de-code-et-outils/01-Cours/Analyse-de-code-et-securite-des-outils.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une injection de commandes apparaît lorsqu’une entrée devient une partie de la syntaxe interprétée par un shell. AST (Abstract Syntax Tree, arbre syntaxique abstrait) représente la structure d’un programme sans avoir à l’exécuter. Un appel suspect constitue un indice à examiner avec le flux de données.

<details>
<summary>Comprendre simplement</summary>
<p>Avant de transmettre un ordre à un opérateur, on vérifie qu’une note du client n’a pas été collée à la place d’une instruction.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
python3 - <<'PY'
import ast
from pathlib import Path
arbre = ast.parse(Path("travail/code-a-auditer.txt").read_text())
for noeud in ast.walk(arbre):
    if isinstance(noeud, ast.Call):
        print("ligne", noeud.lineno, ast.unparse(noeud))
PY
```

ast.parse analyse la syntaxe seulement. Le suffixe .txt rappelle que l’échantillon est un support d’analyse et ne doit pas être exécuté.

### 3. Interpréter

L’étudiant repère la concaténation d’une entrée avec shell=True et décrit le chemin de l’entrée vers l’interpréteur.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Écrire dans le rapport une version utilisant une fonction Python adaptée ou une liste d’arguments avec shell=False, plus une validation adaptée aux besoins.

## Défi autonome

Distinguer détection syntaxique et preuve d’exploitabilité : montrer un faux positif possible d’un simple grep.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Remplacer un caractère spécial ne garantit pas que tous les modes d’interprétation sont supprimés.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab29`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Remplacer un caractère spécial ne garantit pas que tous les modes d’interprétation sont supprimés.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Python — sécurité des sous-processus](https://docs.python.org/3/library/subprocess.html#security-considerations).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
