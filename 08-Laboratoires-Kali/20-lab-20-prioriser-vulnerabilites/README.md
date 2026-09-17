---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 20
semaine_associee: 5
duree_minutes_indicative: 45
---

# Laboratoire 20 — Prioriser trois constats sans inventer de risque

## Mission et contexte

Classer trois constats de l’Atelier Boréal et expliquer pourquoi une version supposée ne devient pas automatiquement le premier correctif.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3, éditeur.
- Mode : Analyse de données synthétiques.
- Lire la [théorie associée à la semaine 5](../../02-Semaines/Semaine-05-Analyse-des-vulnerabilites/01-Cours/Analyse-et-priorisation-des-vulnerabilites.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

La priorité dépend de la preuve, de l’exposition, de l’impact et du contexte métier. Un score technique n’est pas une décision métier complète. Il faut distinguer une faiblesse démontrée d’une hypothèse issue d’un outil.

<details>
<summary>Comprendre simplement</summary>
<p>Une fuite d’eau constatée et une étiquette ancienne sur un tuyau ne justifient pas la même conclusion.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
python3 -m json.tool travail/inventaire.json
cp travail/rapport-modele.md travail/preuves/lab20-triage.md
python3 - <<'PY'
import json
from pathlib import Path
for item in json.loads(Path("travail/inventaire.json").read_text()):
    print(item["id"], "DÉMONTRÉ" if item["preuve"] else "À CONFIRMER", item["impact"])
PY
```

Le fichier est un scénario et non un résultat de scan. Le champ preuve exprime une donnée du scénario ; une véritable mission demanderait les pièces correspondantes.

### 3. Interpréter

Un ordre argumenté, une incertitude explicite et un prochain test sont proposés pour chaque constat.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Ajouter à chaque ligne un responsable fictif, une action concrète et un critère de contre-test, sans inventer de date contractuelle.

## Défi autonome

Faire changer l’exposition d’un actif dans une copie et réévaluer la priorité.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Deux ordres différents peuvent être défendables si leurs hypothèses métier sont explicites.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab20`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Deux ordres différents peuvent être défendables si leurs hypothèses métier sont explicites.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — guide de test web](https://owasp.org/www-project-web-security-testing-guide/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
