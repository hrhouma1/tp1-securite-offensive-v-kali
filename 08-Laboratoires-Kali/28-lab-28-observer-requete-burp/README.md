---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 28
semaine_associee: 7
duree_minutes_indicative: 55
---

# Laboratoire 28 — Observer et rejouer une requête avec Burp Suite

## Mission et contexte

Faire passer uniquement une requête locale par Burp puis modifier un paramètre dans Repeater, l’outil de répétition de requêtes.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Burp Suite Community, curl.
- Mode : Interface graphique Kali et service local.
- Lire la [théorie associée à la semaine 7](../../02-Semaines/Semaine-07-Securite-des-applications-web/01-Cours/Vulnerabilites-et-protection-des-applications-web.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 55 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Un proxy intercepte les échanges qui lui sont explicitement adressés. Il aide à examiner et à rejouer une requête sans modifier le serveur. Rejouer une requête d’une autre origine ou portant des cookies personnels sortirait du périmètre.

<details>
<summary>Comprendre simplement</summary>
<p>Une vitre de contrôle permet de voir une enveloppe passer et d’en envoyer une copie autorisée.</p>
</details>

## Vocabulaire utile

- HTTP (Hypertext Transfer Protocol, protocole de transfert hypertexte).

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
# Dans Burp : Proxy > Settings > Proxy listeners.
# Ajouter un listener sur 127.0.0.1:8082 ; ne pas utiliser 8080, occupé par l'atelier.
# Mettre Intercept sur Off pour le premier essai.
curl --noproxy '' --proxy http://127.0.0.1:8082 'http://127.0.0.1:8080/facture?id=101'
# Dans HTTP history : envoyer cette requête vers Repeater.
# Remplacer seulement id=101 par id=202, puis Send.
```

--proxy impose le proxy local et --noproxy '' empêche une exclusion automatique de localhost. Aucune installation de certificat n’est nécessaire pour ce trafic HTTP local.

### 3. Interpréter

Les deux requêtes sont visibles avec leurs réponses ; la comparaison porte sur les factures fictives.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Rejouer contre /facture-corrige et expliquer pourquoi l’observation d’un proxy n’accorde aucun droit supplémentaire.

## Défi autonome

Exporter uniquement les requêtes de l’atelier et vérifier l’absence de cookies ou d’historiques personnels.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>En cas de blocage, vérifier le listener 8082 et la position du bouton Intercept, sans changer le service d’application.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab28`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

En cas de blocage, vérifier le listener 8082 et la position du bouton Intercept, sans changer le service d’application.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Burp Proxy — PortSwigger](https://portswigger.net/burp/documentation/desktop/tools/proxy).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
