---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 27
semaine_associee: 7
duree_minutes_indicative: 45
---

# Laboratoire 27 — Bloquer une traversée de répertoires

## Mission et contexte

Lire la notice publique, observer un accès indu à un fichier fictif voisin, puis démontrer le blocage.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : curl, pathlib.
- Mode : Service local requis.
- Lire la [théorie associée à la semaine 7](../../02-Semaines/Semaine-07-Securite-des-applications-web/01-Cours/Vulnerabilites-et-protection-des-applications-web.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une traversée de répertoires exploite une entrée qui influence un chemin. Normaliser un chemin ne suffit pas : il faut vérifier que la destination normalisée reste dans le dossier autorisé. Le serveur de ce cours conserve même sa version vulnérable à l’intérieur du dossier de données fictives.

<details>
<summary>Comprendre simplement</summary>
<p>La réception peut autoriser l’accès à la bibliothèque publique sans autoriser la réserve située juste à côté.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
curl --noproxy '*' -sS -G --data-urlencode 'fichier=notice.txt' http://127.0.0.1:8080/telecharger
curl --noproxy '*' -sS -G --data-urlencode 'fichier=../prive/strategie.txt' http://127.0.0.1:8080/telecharger
curl --noproxy '*' -i -G --data-urlencode 'fichier=../prive/strategie.txt' http://127.0.0.1:8080/telecharger-corrige
```

Les deux fichiers appartiennent au jeu de données. Ne pas remplacer la cible par un fichier système ou personnel : le but est de démontrer le défaut sur des données connues.

### 3. Interpréter

Le fichier privé fictif est visible dans la version permissive et refusé avec un statut 403 dans la version corrigée.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Lire l’usage de resolve et is_relative_to dans outils/serveur.py. Ajouter au rapport un test positif sur notice.txt pour éviter une correction qui bloque tout.

## Défi autonome

Expliquer pourquoi un lien symbolique exige lui aussi une vérification de destination résolue.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Comparer les bornes travail et travail/public plutôt que de chercher uniquement la chaîne .. dans l’entrée.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab27`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Comparer les bornes travail et travail/public plutôt que de chercher uniquement la chaîne .. dans l’entrée.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — traversée de répertoires](https://community.owasp.org/attacks/Path_Traversal).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
