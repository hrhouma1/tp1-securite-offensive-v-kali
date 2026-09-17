---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 44
semaine_associee: 12
duree_minutes_indicative: 60
---

# Laboratoire 44 — Observer la messagerie d’un objet connecté fictif

## Mission et contexte

Publier une mesure fictive sur un courtier limité à la boucle locale et observer l’abonnement, puis analyser une mauvaise pratique de secrets dans les messages.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Mosquitto, mosquitto_pub, mosquitto_sub.
- Mode : Courtier local — aucun objet physique.
- Lire la [théorie associée à la semaine 12](../../02-Semaines/Semaine-12-Securite-cloud-mobile-et-objets-connectes/01-Cours/Securite-du-cloud-du-mobile-et-des-objets-connectes.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 60 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

MQTT (Message Queuing Telemetry Transport, protocole léger de publication et d’abonnement) fait circuler des messages via un courtier. Un sujet organise les échanges mais n’est pas une protection d’accès. Autoriser une connexion anonyme facilite la démonstration, pas une mise en production.

<details>
<summary>Comprendre simplement</summary>
<p>Un panneau d’annonces par rubrique devient public si tout le monde peut lire et écrire les rubriques.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
# Terminal A : arrêter avec Ctrl+C en fin d'atelier.
mosquitto -c travail/mosquitto-local.conf -v
# Terminal B :
mosquitto_sub -h 127.0.0.1 -p 18883 -t 'atelier/temperature' -C 1 -W 30
# Terminal C, avant la fin des 30 secondes :
mosquitto_pub -h 127.0.0.1 -p 18883 -t 'atelier/temperature' -m '21'
# Après réception :
python3 -m json.tool travail/objet-connecte.json
```

-C 1 termine l’abonnement après un message et -W 30 borne l’attente. Le fichier de configuration fixe listener 18883 127.0.0.1 ; ne pas le remplacer par une écoute réseau.

### 3. Interpréter

Le terminal abonné reçoit 21. Le scénario identifie un mot de passe usine, une absence de mises à jour et un faux jeton dans un sujet de configuration.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Proposer authentification, droits par sujet, chiffrement des échanges et procédure de mise à jour. Ne publier aucun secret, même dans un sujet au nom discret.

## Défi autonome

Tester un abonnement à un autre sujet et expliquer l’absence de message sans conclure à une panne réseau.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Si 18883 est déjà occupé, identifier le service existant et demander à l’enseignant un port local disponible ; ne pas arrêter un service inconnu.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab44`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Si 18883 est déjà occupé, identifier le service existant et demander à l’enseignant un port local disponible ; ne pas arrêter un service inconnu.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Eclipse Mosquitto — configuration](https://mosquitto.org/man/mosquitto-conf-5.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
