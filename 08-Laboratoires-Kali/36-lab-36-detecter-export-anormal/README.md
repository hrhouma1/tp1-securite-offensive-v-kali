---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 36
semaine_associee: 11
duree_minutes_indicative: 45
---

# Laboratoire 36 — Détecter un export inhabituel dans des traces

## Mission et contexte

Repérer l’événement volumineux, calculer sa part dans le volume observé et dire quelles preuves manquent pour conclure.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3.
- Mode : Analyse de journaux synthétiques.
- Lire la [théorie associée à la semaine 11](../../02-Semaines/Semaine-11-Mouvements-lateraux-et-exfiltration/01-Cours/Segmentation-mouvements-lateraux-et-exfiltration.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

L’exfiltration suppose une sortie non autorisée de données ; un gros volume n’en est qu’un indice possible. Un seuil doit être expliqué et comparé au contexte. Les journaux fournis décrivent un export fictif, sans destinataire réseau réel.

<details>
<summary>Comprendre simplement</summary>
<p>Voir un grand camion quitter un entrepôt mérite une vérification, mais peut correspondre à une livraison prévue.</p>
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
lignes = [json.loads(x) for x in Path("travail/evenements.jsonl").read_text().splitlines()]
total = sum(x["octets"] for x in lignes)
for x in lignes:
    if x["octets"] > 1000000:
        print(x["heure"], x["compte"], x["action"], x["octets"], round(100*x["octets"]/total, 2))
print("Total observé :", total)
PY
```

JSONL (JSON Lines, une donnée JSON par ligne) facilite la lecture événement par événement. Le seuil d’un million d’octets est un choix d’exercice, pas une règle universelle.

### 3. Interpréter

Un export de 8 000 000 octets est isolé ; la conclusion reconnaît l’absence de preuve de destination ou d’autorisation.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Proposer une collecte minimale complémentaire : destinataire, autorisation métier et volume habituel, sans collecter le contenu complet par défaut.

## Défi autonome

Modifier un seuil sur une copie et discuter les faux positifs et les événements manqués.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Employer « export inhabituel dans le scénario », pas « vol confirmé ».</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab36`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Employer « export inhabituel dans le scénario », pas « vol confirmé ».

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Python — fonctions d’empreinte et de dérivation](https://docs.python.org/3/library/hashlib.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
