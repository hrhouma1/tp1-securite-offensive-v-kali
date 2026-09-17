---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 21
semaine_associee: 7
duree_minutes_indicative: 35
---

# Laboratoire 21 — Lire une requête et une réponse HTTP

## Mission et contexte

Comparer une route existante et une route absente, puis séparer les en-têtes du contenu enregistré.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : curl, Python 3.
- Mode : Service local requis.
- Lire la [théorie associée à la semaine 7](../../02-Semaines/Semaine-07-Securite-des-applications-web/01-Cours/Vulnerabilites-et-protection-des-applications-web.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 35 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

HTTP (Hypertext Transfer Protocol, protocole de transfert hypertexte) distingue notamment la méthode, le chemin, les en-têtes et le corps. Un statut 200 indique le traitement réussi de la requête selon le serveur ; il ne prouve pas que l’action est sûre.

<details>
<summary>Comprendre simplement</summary>
<p>Le serveur reçoit une enveloppe : l’adresse, les consignes et la lettre sont des parties différentes.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
curl --noproxy '*' -sS -D travail/preuves/lab21-entetes.txt -o travail/preuves/lab21-corps.json http://127.0.0.1:8080/health
python3 -m json.tool travail/preuves/lab21-corps.json
curl --noproxy '*' -i http://127.0.0.1:8080/inexistante
```

-D enregistre les en-têtes ; -o enregistre le corps ; -i les affiche ensemble. JSON (JavaScript Object Notation, notation structurée de données) est le format du corps de /health.

### 3. Interpréter

La route de santé répond 200 et la route inexistante 404. Les deux types d’informations sont enregistrés séparément.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Décrire les statuts qu’un service devrait utiliser pour une authentification absente, une autorisation refusée et une limitation d’essais.

## Défi autonome

Comparer curl sans --fail et avec --fail sur /inexistante, puis observer le code de sortie.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Le code de sortie de curl n’est pas nécessairement le statut HTTP : une réponse 404 peut être transportée correctement.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab21`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Le code de sortie de curl n’est pas nécessairement le statut HTTP : une réponse 404 peut être transportée correctement.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [curl — manuel](https://curl.se/docs/manpage.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
