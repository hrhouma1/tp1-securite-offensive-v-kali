---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 22
semaine_associee: 7
duree_minutes_indicative: 50
---

# Laboratoire 22 — Tester un formulaire fictif avec Hydra

## Mission et contexte

Retrouver le mot de passe d’un unique compte d’exercice avec la petite liste fournie, puis valider manuellement le résultat.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Hydra, curl.
- Mode : Service local requis — sept candidats maximum.
- Lire la [théorie associée à la semaine 7](../../02-Semaines/Semaine-07-Securite-des-applications-web/01-Cours/Vulnerabilites-et-protection-des-applications-web.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 50 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une recherche en ligne envoie les essais à un service, contrairement au test d’une empreinte hors ligne. Le critère d’échec doit correspondre à la réponse réelle de l’application. Un mauvais critère peut produire de faux succès.

<details>
<summary>Comprendre simplement</summary>
<p>Cette fois, chaque clé est présentée au guichet ; le guichet peut compter les essais et refuser de continuer.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
curl --noproxy '*' -i -d 'utilisateur=etudiant&motdepasse=incorrect' http://127.0.0.1:8080/connexion
hydra -l etudiant -P travail/mots.txt -s 8080 -t 1 -f -o travail/preuves/lab22-hydra.txt 127.0.0.1 http-post-form '/connexion:utilisateur=^USER^&motdepasse=^PASS^:F=Identifiants incorrects'
curl --noproxy '*' -i -d 'utilisateur=etudiant&motdepasse=CANDIDAT_RETROUVE' http://127.0.0.1:8080/connexion
```

-l fixe un compte ; -P utilise seulement les sept mots fictifs ; -s fixe le port ; -t 1 limite la concurrence ; -f arrête au premier succès. Remplacer le candidat dans la dernière commande. Ne pas employer rockyou.txt sur ce formulaire.

### 3. Interpréter

Un essai manuel négatif, un candidat identifié et une confirmation manuelle positive sont conservés.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Comparer avec le point d’entrée limité au laboratoire suivant ; recommander une défense qui ne dépend pas de cacher le formulaire.

## Défi autonome

Modifier volontairement le critère d’échec sur une copie de la commande avec un seul candidat erroné, puis expliquer le faux positif sans augmenter le nombre d’essais.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Vérifier exactement la chaîne Identifiants incorrects avant de paramétrer Hydra.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab22`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Vérifier exactement la chaîne Identifiants incorrects avant de paramétrer Hydra.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Hydra — Kali](https://www.kali.org/tools/hydra/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
