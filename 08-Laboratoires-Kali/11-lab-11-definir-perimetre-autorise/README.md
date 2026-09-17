---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 11
semaine_associee: 2
duree_minutes_indicative: 35
---

# Laboratoire 11 — Bloquer une cible hors du mandat

## Mission et contexte

Créer un garde-fou qui accepte uniquement l’adresse de boucle locale du laboratoire, avant toute utilisation d’un outil de test.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3, JSON.
- Mode : Analyse et test local.
- Lire la [théorie associée à la semaine 2](../../02-Semaines/Semaine-02-Planification-et-regles-engagement/01-Cours/Planification-et-regles-engagement.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 35 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Le périmètre décrit précisément les actifs, les actions et les limites autorisés. Une adresse privée n’accorde pas une autorisation. JSON (JavaScript Object Notation, notation structurée de données) permet ici de représenter une liste de cibles admises.

<details>
<summary>Comprendre simplement</summary>
<p>Posséder un passe d’atelier n’autorise pas à ouvrir toutes les portes du quartier.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
python3 -m json.tool travail/mandat.json
python3 - <<'PY'
import json
from pathlib import Path
mandat = json.loads(Path("travail/mandat.json").read_text())
for cible in ["127.0.0.1", "192.0.2.20", "example.com"]:
    print(cible, "AUTORISÉE" if cible in mandat["cibles_autorisees"] else "REFUSÉE")
PY
```

Le script compare des chaînes sans résoudre de nom et sans contacter les cibles refusées. IP (Internet Protocol, protocole Internet) désigne ici le type d’adresse utilisé.

### 3. Interpréter

Seule 127.0.0.1 est acceptée. Les autres valeurs restent des exemples non contactés.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Ajouter par écrit un point d’arrêt, un plafond d’essais et la procédure à suivre si un résultat sort du cadre.

## Défi autonome

Ajouter un contrôle du port et montrer qu’un port non listé est refusé sans connexion.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Ne pas employer « toutes les adresses privées » comme liste autorisée.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab11`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Ne pas employer « toutes les adresses privées » comme liste autorisée.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Python — fonctions d’empreinte et de dérivation](https://docs.python.org/3/library/hashlib.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
