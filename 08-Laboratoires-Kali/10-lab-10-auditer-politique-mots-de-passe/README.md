---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 10
semaine_associee: 2
duree_minutes_indicative: 40
---

# Laboratoire 10 — Concevoir une politique de mots de passe défendable

## Mission et contexte

Évaluer les mots fictifs du scénario et proposer des règles qui ne récompensent pas simplement les substitutions prévisibles.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3, éditeur de texte.
- Mode : Analyse et expérimentation locale.
- Lire la [théorie associée à la semaine 2](../../02-Semaines/Semaine-02-Planification-et-regles-engagement/01-Cours/Planification-et-regles-engagement.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 40 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

La résistance d’un secret dépend de la façon dont il est choisi, pas seulement des catégories de caractères visibles. La réutilisation et la prévisibilité contextuelle restent importantes. MFA (Multi-Factor Authentication, authentification multifacteur) ajoute des facteurs distincts, mais ne transforme pas un stockage faible en stockage robuste.

<details>
<summary>Comprendre simplement</summary>
<p>Une porte gagne à avoir plusieurs protections indépendantes ; ajouter plusieurs étiquettes au même cadenas n’ajoute pas plusieurs serrures.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
python3 - <<'PY'
from pathlib import Path
for mot in Path("travail/mots.txt").read_text().splitlines():
    print(len(mot), any(c.isupper() for c in mot), any(c.isdigit() for c in mot), mot)
PY
cp travail/rapport-modele.md travail/preuves/lab10-politique.md
```

Le script décrit longueur, présence de majuscule et présence de chiffre ; il ne mesure pas une entropie réelle. Les mots affichés sont tous fictifs.

### 3. Interpréter

Le rapport montre au moins un mot satisfaisant une règle de composition mais restant facile à prévoir.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Rédiger une politique : secret unique, refus des choix courants, gestionnaire de mots de passe, contrôle des tentatives, authentification multifacteur adaptée et procédure de récupération. Distinguer contrôles du service et pratiques utilisateur.

## Défi autonome

Présenter la politique en 90 secondes à une direction fictive, avec deux bénéfices et une contrainte d’usage.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Ne pas calculer une entropie en supposant un tirage aléatoire pour un mot choisi par un humain.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab10`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Ne pas calculer une entropie en supposant un tirage aléatoire pour un mot choisi par un humain.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — authentification](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
