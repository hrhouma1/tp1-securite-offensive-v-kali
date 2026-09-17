---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 17
semaine_associee: 5
duree_minutes_indicative: 40
---

# Laboratoire 17 — Distinguer bannière et vulnérabilité

## Mission et contexte

Comparer ce que le serveur annonce à ce que Nmap infère, puis rédiger un constat sans surinterprétation.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : curl, Nmap.
- Mode : Service local requis.
- Lire la [théorie associée à la semaine 5](../../02-Semaines/Semaine-05-Analyse-des-vulnerabilites/01-Cours/Analyse-et-priorisation-des-vulnerabilites.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 40 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une bannière est une information déclarée par un service. Elle peut être modifiée, incomplète ou sans rapport avec les correctifs installés. Détecter une chaîne de version ne démontre donc pas à lui seul une vulnérabilité exploitable.

<details>
<summary>Comprendre simplement</summary>
<p>L’étiquette sur une boîte aide à l’identifier, mais ne remplace pas l’examen de son contenu.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
curl --noproxy '*' -sSI http://127.0.0.1:8080/
nmap -sT -sV --version-light -Pn -n -p 8080 --host-timeout 30s 127.0.0.1
grep -n 'server_version' outils/serveur.py
```

-I demande les en-têtes ; -sV active les sondes d’identification ; --version-light réduit leur nombre. Le code source local sert ici à comparer déclaration et implémentation.

### 3. Interpréter

La chaîne BorealLabs/1.0 est visible dans la réponse. L’identification exacte de Nmap peut varier.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Rédiger « bannière observée » et proposer une vérification complémentaire avant toute attribution de vulnérabilité.

## Défi autonome

Sur une copie du serveur, changer seulement la bannière et expliquer pourquoi la sécurité réelle n’a pas nécessairement changé.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Ne pas inventer de CVE (Common Vulnerabilities and Exposures, identifiant public de vulnérabilité) pour le nom fictif.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab17`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Ne pas inventer de CVE (Common Vulnerabilities and Exposures, identifiant public de vulnérabilité) pour le nom fictif.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Nmap — techniques de scan](https://nmap.org/book/man-port-scanning-techniques.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
