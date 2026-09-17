---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 14
semaine_associee: 3
duree_minutes_indicative: 40
---

# Laboratoire 14 — Cartographier une zone DNS sans interroger Internet

## Mission et contexte

Dessiner les relations entre les noms du fichier de zone et signaler les éléments qui demanderaient une validation autorisée.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : grep, éditeur.
- Mode : Analyse de configuration synthétique.
- Lire la [théorie associée à la semaine 3](../../02-Semaines/Semaine-03-Renseignement-sources-ouvertes/01-Cours/Renseignement-et-reconnaissance-passive.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 40 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

DNS (Domain Name System, système de noms de domaine) associe des noms à des informations telles que des adresses ou des alias. Un enregistrement A porte une adresse IPv4 ; CNAME (Canonical Name, nom canonique) représente un alias. Une zone fournie n’est pas une réponse réseau actuelle.

<details>
<summary>Comprendre simplement</summary>
<p>Un annuaire peut relier un surnom à une entrée principale ; lire l’annuaire ne prouve pas que la personne est présente.</p>
</details>

## Vocabulaire utile

- IPv4 (Internet Protocol version 4, protocole Internet version 4).

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
grep -nE 'SOA|NS|A |CNAME|ORIGIN|TTL' travail/zone.txt
sha256sum travail/zone.txt
cp travail/zone.txt travail/copies/lab14-zone.txt
```

SOA (Start of Authority, début d’autorité) décrit des paramètres administratifs. NS (Name Server, serveur de noms) désigne le serveur de la zone. TTL (Time To Live, durée de vie) indique une durée de cache.

### 3. Interpréter

factures est identifié comme alias de portail, et les deux adresses restent des valeurs documentaires non contactées.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Annoter la copie avec le nom pleinement qualifié de chaque entrée et expliquer le rôle des points finaux.

## Défi autonome

Expliquer pourquoi un alias n’est pas un deuxième serveur prouvé.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Le nom d’origine boreal.example. s’applique aux noms relatifs.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab14`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Le nom d’origine boreal.example. s’applique aux noms relatifs.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [RFC 1035 — système de noms de domaine](https://www.rfc-editor.org/rfc/rfc1035.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
