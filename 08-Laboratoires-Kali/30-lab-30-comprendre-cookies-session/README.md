---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 30
semaine_associee: 7
duree_minutes_indicative: 45
---

# Laboratoire 30 — Comprendre les cookies de session et leurs limites

## Mission et contexte

Observer une réponse sans session puis une réponse avec le cookie d’exercice, et relever les limites du mécanisme fourni.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : curl.
- Mode : Service local requis — jeton simulé.
- Lire la [théorie associée à la semaine 7](../../02-Semaines/Semaine-07-Securite-des-applications-web/01-Cours/Vulnerabilites-et-protection-des-applications-web.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Un cookie peut transporter un identifiant de session. HttpOnly limite l’accès par les scripts du navigateur, SameSite encadre certains envois intersites et Secure réserve l’envoi aux connexions sécurisées. Aucune de ces options ne rend sûr un jeton prévisible.

<details>
<summary>Comprendre simplement</summary>
<p>Le bracelet d’accès doit être difficile à contrefaire ; limiter où il peut être présenté ne corrige pas un numéro identique pour tous.</p>
</details>

## Vocabulaire utile

- TLS (Transport Layer Security, sécurité de la couche de transport).

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
curl --noproxy '*' -i http://127.0.0.1:8080/session
curl --noproxy '*' -i -c travail/preuves/lab30-cookies.txt -d 'utilisateur=etudiant&motdepasse=velo2026' http://127.0.0.1:8080/connexion
curl --noproxy '*' -i -b travail/preuves/lab30-cookies.txt http://127.0.0.1:8080/session
```

-c enregistre un fichier de cookies fictifs ; -b le renvoie. La chaîne de session du serveur est fixe à des fins pédagogiques : elle ne constitue pas un exemple de gestion de session de production.

### 3. Interpréter

Le premier accès répond 401 et le dernier 200. L’en-tête Set-Cookie est identifié et ses attributs sont expliqués.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Décrire un jeton aléatoire, une expiration, une invalidation à la déconnexion, une protection contre CSRF (Cross-Site Request Forgery, falsification de requête intersite) et l’usage de TLS avec Secure en production.

## Défi autonome

Supprimer le cookie uniquement de la commande de test et constater le retour à 401, sans modifier le navigateur personnel.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Les routes de factures utilisent une identité simulée indépendante ; ne pas prétendre avoir testé leur authentification grâce à ce cookie.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab30`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Les routes de factures utilisent une identité simulée indépendante ; ne pas prétendre avoir testé leur authentification grâce à ce cookie.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — gestion des sessions](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
