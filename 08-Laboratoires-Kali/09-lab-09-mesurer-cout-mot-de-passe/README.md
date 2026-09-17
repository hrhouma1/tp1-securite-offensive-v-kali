---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 9
semaine_associee: 10
duree_minutes_indicative: 40
---

# Laboratoire 09 — Mesurer le coût d’une fonction de dérivation

## Mission et contexte

Quantifier la différence observée entre une empreinte rapide et une dérivation, puis formuler une conclusion limitée aux mesures réalisées.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3, hashlib.
- Mode : Manipulation hors ligne.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 40 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

PBKDF2 (Password-Based Key Derivation Function 2, fonction de dérivation de clé à partir d’un mot de passe) répète un traitement paramétrable. Le temps par candidat influence le coût d’une recherche hors ligne. Une mesure dans une machine virtuelle dépend de la charge et ne prédit pas directement la vitesse d’un attaquant.

<details>
<summary>Comprendre simplement</summary>
<p>Si chaque clé exige une opération supplémentaire avant l’essai, tester tout le trousseau prend plus de temps, mais une clé évidente reste évidente.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
python3 outils/mesurer-derivation.py
python3 outils/mesurer-derivation.py
python3 outils/mesurer-derivation.py
```

Le script rapporte un temps moyen par calcul pour deux charges différentes. Le paramètre de 100 000 itérations sert à l’expérience et ne constitue pas une recommandation de production.

### 3. Interpréter

Trois mesures et leur variabilité sont consignées. La dérivation est normalement nettement plus coûteuse que l’empreinte simple.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Proposer de calibrer une bibliothèque reconnue selon les recommandations à jour, les ressources du service et la résistance recherchée, sans recopier arbitrairement le paramètre du laboratoire.

## Défi autonome

Sur une copie du script, doubler les itérations et vérifier l’ordre de grandeur de l’évolution du coût.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Comparer des temps par calcul, pas les durées totales de boucles ayant des nombres d’itérations différents.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab09`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Comparer des temps par calcul, pas les durées totales de boucles ayant des nombres d’itérations différents.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Python — fonctions d’empreinte et de dérivation](https://docs.python.org/3/library/hashlib.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
