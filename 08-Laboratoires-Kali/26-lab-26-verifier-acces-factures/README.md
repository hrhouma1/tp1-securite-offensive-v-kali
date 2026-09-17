---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 26
semaine_associee: 7
duree_minutes_indicative: 45
---

# Laboratoire 26 — Empêcher l’accès à la facture d’un autre client

## Mission et contexte

Comparer l’accès à sa facture et à une facture tierce dans deux versions de la même application.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : curl.
- Mode : Service local requis — identité Alice simulée.
- Lire la [théorie associée à la semaine 7](../../02-Semaines/Semaine-07-Securite-des-applications-web/01-Cours/Vulnerabilites-et-protection-des-applications-web.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

IDOR (Insecure Direct Object Reference, référence directe non sécurisée à un objet) décrit un défaut de contrôle d’accès à un objet désigné par l’utilisateur. Deviner un numéro n’est pas le problème central : le serveur doit vérifier le droit d’accès pour chaque objet.

<details>
<summary>Comprendre simplement</summary>
<p>Connaître le numéro d’une chambre ne donne pas le droit d’en recevoir la clé.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
curl --noproxy '*' -i 'http://127.0.0.1:8080/facture?id=101'
curl --noproxy '*' -i 'http://127.0.0.1:8080/facture?id=202'
curl --noproxy '*' -i 'http://127.0.0.1:8080/facture-corrige?id=202'
curl --noproxy '*' -i 'http://127.0.0.1:8080/facture-corrige?id=101'
```

L’identité Alice est fixée par la simulation, pas tirée du cookie de connexion du laboratoire 30. Les deux mécanismes sont pédagogiquement séparés.

### 3. Interpréter

La facture tierce est accessible dans la version vulnérable et refusée dans la version corrigée ; la facture d’Alice reste disponible.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Formuler le contrôle d’autorisation côté serveur et un test de non-régression pour chacun des deux propriétaires.

## Défi autonome

Tester un identifiant absent et expliquer la différence entre objet inexistant et accès interdit dans cette simulation.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Un numéro d’objet difficile à deviner ne remplace pas une autorisation.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab26`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Un numéro d’objet difficile à deviner ne remplace pas une autorisation.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — contrôle d’accès aux objets](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
