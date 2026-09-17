---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 25
semaine_associee: 7
duree_minutes_indicative: 45
---

# Laboratoire 25 — Tester l’injection HTML et comprendre le risque XSS

## Mission et contexte

Comparer l’affichage d’une balise inoffensive et montrer que l’encodage corrige l’interprétation inattendue.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : curl, navigateur local.
- Mode : Service local requis.
- Lire la [théorie associée à la semaine 7](../../02-Semaines/Semaine-07-Securite-des-applications-web/01-Cours/Vulnerabilites-et-protection-des-applications-web.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

HTML (HyperText Markup Language, langage de balisage hypertexte) décrit une page. XSS (Cross-Site Scripting, exécution de script injecté dans une page web) nécessite de distinguer une entrée non échappée d’une exécution effectivement obtenue. Ici, la politique CSP (Content Security Policy, politique de sécurité du contenu) bloque les scripts : l’exercice démontre l’injection de balises, pas un vol de session.

<details>
<summary>Comprendre simplement</summary>
<p>Le texte d’un visiteur ne devrait pas pouvoir redessiner les panneaux du bâtiment.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
curl --noproxy '*' -sS -G --data-urlencode 'texte=<b>MESSAGE_FICTIF</b>' http://127.0.0.1:8080/echo
curl --noproxy '*' -sS -G --data-urlencode 'texte=<b>MESSAGE_FICTIF</b>' http://127.0.0.1:8080/echo-corrige
curl --noproxy '*' -sS -D - -o /dev/null http://127.0.0.1:8080/echo
```

La première réponse inclut les balises saisies ; la seconde les transforme en texte affichable. Pour voir la différence, ouvrir les mêmes routes dans le navigateur local en encodant les paramètres.

### 3. Interpréter

Le rapport distingue balise interprétée, texte échappé et restriction d’exécution portée par la politique de contenu.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Expliquer pourquoi l’échappement adapté au contexte reste nécessaire même avec une politique de contenu restrictive.

## Défi autonome

Tester le caractère & et les guillemets, puis expliquer pourquoi les contextes HTML, attribut et script n’emploient pas tous le même encodage.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Ne pas conclure « exécution JavaScript démontrée » à partir d’un texte simplement affiché en gras.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab25`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Ne pas conclure « exécution JavaScript démontrée » à partir d’un texte simplement affiché en gras.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — encodage et prévention XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
