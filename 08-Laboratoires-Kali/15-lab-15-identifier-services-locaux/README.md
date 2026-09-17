---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 15
semaine_associee: 4
duree_minutes_indicative: 35
---

# Laboratoire 15 — Associer un port à son processus

## Mission et contexte

Retrouver le serveur d’exercice dans la liste des sockets et démontrer qu’il écoute uniquement en boucle locale.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : ss, ps, curl.
- Mode : Service local requis.
- Lire la [théorie associée à la semaine 4](../../02-Semaines/Semaine-04-Reconnaissance-active-et-cartographie/01-Cours/Reconnaissance-active-et-cartographie-reseau.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 35 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Un port en écoute indique qu’un programme attend des connexions. TCP (Transmission Control Protocol, protocole de contrôle de transmission) fournit ici le transport du service web. Une écoute sur 127.0.0.1 n’est pas équivalente à une écoute sur toutes les interfaces.

<details>
<summary>Comprendre simplement</summary>
<p>Un guichet ouvert à l’intérieur d’une pièce n’est pas nécessairement accessible depuis la rue.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
ss -lntp 'sport = :8080'
ps -ef | grep '[o]utils/serveur.py'
curl --noproxy '*' --max-time 3 http://127.0.0.1:8080/health
```

ss -lntp demande les sockets en écoute, sous forme numérique, en TCP, avec les processus accessibles. Le PID (Process Identifier, identifiant de processus) peut être masqué selon les permissions.

### 3. Interpréter

Une écoute 127.0.0.1:8080 et une réponse du point de santé sont observées.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Arrêter le serveur avec Ctrl+C, refaire ss, puis le relancer. Documenter la différence.

## Défi autonome

Lancer la même application sur 8081 dans un second terminal et identifier les deux processus.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Ne pas remplacer l’adresse d’écoute par 0.0.0.0 pour résoudre un problème de connexion.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab15`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Ne pas remplacer l’adresse d’écoute par 0.0.0.0 pour résoudre un problème de connexion.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Nmap — techniques de scan](https://nmap.org/book/man-port-scanning-techniques.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
