---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 35
semaine_associee: 11
duree_minutes_indicative: 50
---

# Laboratoire 35 — Couper un chemin de mouvement latéral dans un modèle

## Mission et contexte

Trouver un chemin entre le poste et la sauvegarde dans le modèle, puis démontrer sa disparition après restriction.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3.
- Mode : Simulation de segmentation — aucun réseau distant.
- Lire la [théorie associée à la semaine 11](../../02-Semaines/Semaine-11-Mouvements-lateraux-et-exfiltration/01-Cours/Segmentation-mouvements-lateraux-et-exfiltration.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 50 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

La segmentation limite les communications autorisées entre zones. Un graphe de connexions représente une partie du problème, mais pas les identités, vulnérabilités ni protections réelles. Un chemin dans le graphe est une possibilité de circulation, pas une compromission prouvée.

<details>
<summary>Comprendre simplement</summary>
<p>Retirer une porte entre deux couloirs peut empêcher un passage direct, sans prouver que toutes les fenêtres sont fermées.</p>
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
python3 - <<'PY'
import json
from pathlib import Path
modele = json.loads(Path("travail/segments.json").read_text())
def atteignable(liens, origine, cible):
    vus, attente = set(), [origine]
    while attente:
        courant = attente.pop()
        if courant == cible:
            return True
        if courant in vus:
            continue
        vus.add(courant)
        attente.extend(b for a, b in liens if a == courant)
    return False
for cle in ["liaisons", "politique_cible"]:
    print(cle, atteignable(modele[cle], "poste", "sauvegarde"))
PY
```

Le script parcourt un graphe orienté fourni comme JSON. Il ne crée ni tunnel, ni pare-feu, ni connexion entre machines.

### 3. Interpréter

Le chemin existe dans le premier modèle et n’existe plus dans la politique cible.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Justifier la suppression de web vers comptabilite et discuter les échanges métier à conserver.

## Défi autonome

Ajouter une liaison alternative dans une copie et montrer pourquoi il faut chercher tous les chemins pertinents.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Les liens sont orientés : ne pas ajouter automatiquement leur inverse.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab35`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Les liens sont orientés : ne pas ajouter automatiquement leur inverse.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — guide de test web](https://owasp.org/www-project-web-security-testing-guide/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
