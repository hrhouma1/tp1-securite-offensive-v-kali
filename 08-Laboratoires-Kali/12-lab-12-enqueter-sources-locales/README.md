---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 12
semaine_associee: 3
duree_minutes_indicative: 40
---

# Laboratoire 12 — Mener une reconnaissance passive sur un dossier fictif

## Mission et contexte

Extraire les indices présents dans la page fournie et produire un inventaire avec une colonne « observé » et une colonne « à confirmer ».

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : grep, Python 3.
- Mode : Analyse de documents synthétiques.
- Lire la [théorie associée à la semaine 3](../../02-Semaines/Semaine-03-Renseignement-sources-ouvertes/01-Cours/Renseignement-et-reconnaissance-passive.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 40 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

La reconnaissance passive réunit des informations sans tester activement le système étudié. Le contexte d’une source et sa date comptent autant que son contenu. Trouver une adresse dans une page ne prouve pas qu’elle est active ni que la personne consent à être contactée.

<details>
<summary>Comprendre simplement</summary>
<p>Lire une affiche dans un dossier d’exercice n’est pas sonner chez les personnes qui y sont mentionnées.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
grep -nE 'Contact|Responsable|title' travail/page.html
python3 - <<'PY'
import re
from pathlib import Path
texte = Path("travail/page.html").read_text()
print([x.rstrip(".") for x in re.findall(r"[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+", texte)])
PY
sha256sum travail/page.html
```

grep conserve les numéros de ligne. L’expression régulière extrait des chaînes ressemblant à des adresses ; elle ne valide pas l’existence des boîtes.

### 3. Interpréter

Un nom d’organisation, un rôle et une adresse fictive sont reliés à une source locale identifiée.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Réduire dans une copie les renseignements non nécessaires à une page publique et justifier chaque retrait.

## Défi autonome

Faire échanger les inventaires entre binômes et rechercher une conclusion qui dépasse les preuves.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Le domaine .example sert à la documentation ; ne pas essayer d’envoyer un message.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab12`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Le domaine .example sert à la documentation ; ne pas essayer d’envoyer un message.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Python — fonctions d’empreinte et de dérivation](https://docs.python.org/3/library/hashlib.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
