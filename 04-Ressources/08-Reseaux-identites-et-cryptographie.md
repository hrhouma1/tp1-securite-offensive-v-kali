---
tags: [cours, approfondissement]
maj: 2026-09-13
statut: rédigé
---

# Réseaux, identités et cryptographie — approfondissements théoriques

Cette annexe développe les prérequis qui reviennent dans plusieurs semaines. Elle complète le cours sans modifier le plan officiel.

## 1. Encapsulation et couches de communication

Une application construit un message. Le transport ajoute les informations nécessaires à sa communication. Le réseau ajoute les adresses d'acheminement. Le lien local permet de transmettre sur le réseau immédiat.

Lors de la réception, les couches sont interprétées dans l'ordre inverse. Une erreur observée à un niveau n'identifie pas automatiquement la cause à ce même niveau. Une page absente peut provenir d'une résolution de nom, d'une route, d'une connexion ou de l'application.

Le modèle OSI (Open Systems Interconnection, interconnexion de systèmes ouverts) fournit sept couches conceptuelles : physique, liaison, réseau, transport, session, présentation et application. Dans la pratique, les protocoles ne se superposent pas toujours exactement à cette représentation. L'intérêt pédagogique est de poser les questions au bon niveau.

<details>
<summary>Comprendre simplement : le colis et ses emballages</summary>
<p>Le contenu porte le message. L'emballage indique comment le transporter. L'adresse indique où l'acheminer. Ouvrir l'emballage ne transforme pas automatiquement le contenu en une donnée fiable : chaque niveau doit encore être interprété correctement.</p>
</details>

### Exemple de diagnostic par couches

Le navigateur ne joint pas le catalogue. Tester d'abord le service depuis la machine qui l'exécute. S'il répond localement, examiner l'écoute sur l'interface voulue. Si l'écoute est correcte, vérifier les routes et les règles de passage. Si la connexion fonctionne mais le nom échoue, examiner la résolution.

On modifie une condition à la fois. Une intervention qui change simultanément le nom, le port et le pare-feu empêche d'identifier la cause.

## 2. Préfixes, sous-réseaux et routes

Une adresse IPv4 (Internet Protocol version 4, protocole Internet version 4) comporte 32 bits. Un préfixe indique quelle partie identifie le réseau. Dans une notation /24, 24 bits appartiennent au préfixe et 8 bits restent pour les adresses de ce bloc, soit 256 valeurs. Dans un sous-réseau classique, certaines valeurs jouent des rôles particuliers ; le nombre de machines utilisables dépend donc du contexte.

Un poste compare la destination à ses routes. La route la plus spécifique applicable est généralement choisie avant une route moins précise. La route par défaut sert lorsqu'aucune route plus spécifique ne correspond.

Une adresse privée n'est pas routée sur Internet public de la même manière qu'une adresse publique, mais elle peut atteindre des services extérieurs par des mécanismes de traduction ou des relais. Le mot privé ne signifie pas isolé.

La boucle locale désigne la machine elle-même. Dans une machine virtuelle, sa boucle locale est celle de l'invité, pas automatiquement celle de l'hôte.

## 3. Connexion et application

TCP (Transmission Control Protocol, protocole de contrôle de transmission) gère notamment l'ordre et la retransmission. Les accusés de réception concernent la communication, pas l'approbation métier du contenu.

Un serveur peut accepter une connexion puis répondre que l'action est interdite. Un pare-feu peut laisser passer la connexion alors que l'application refuse la facture. Ces contrôles se situent à des niveaux différents.

UDP (User Datagram Protocol, protocole de datagramme utilisateur) n'offre pas le même établissement de connexion. Une application peut cependant construire ses propres mécanismes de fiabilité au-dessus. Ne pas réduire la différence à « fiable » contre « inutile ».

## 4. Les codes de réponse et leur interprétation

Dans HTTP (Hypertext Transfer Protocol, protocole de transfert hypertexte), un code 200 indique généralement le succès de la requête selon le serveur. Un code 403 exprime un refus d'accès ; 404 indique une ressource non trouvée selon la réponse ; 500 indique une erreur côté serveur.

Ces codes ne sont pas des diagnostics de sécurité universels. Une page d'erreur mal conçue peut être renvoyée avec 200. Un serveur peut choisir 404 pour éviter de révéler un objet interdit. Il faut donc lire le comportement et la règle attendue.

Dans l'atelier, les statuts sont volontairement simples : 200 pour une facture accessible, 403 pour le refus de la facture tierce et 404 pour une facture inexistante. Cette convention est locale au programme.

## 5. Cookies, sessions et jetons

Un cookie est un mécanisme de stockage et de transmission de petites valeurs par le navigateur. Le serveur peut l'utiliser pour retrouver une session, mais le cookie n'est pas la session à lui seul.

Une session devrait avoir une durée, un renouvellement et une révocation adaptés. Un changement de mot de passe ne retire pas nécessairement toutes les sessions dans toutes les architectures. Il faut tester ce comportement.

Un jeton signé peut porter des informations vérifiables sans consultation permanente d'une session serveur. La signature protège son intégrité et son origine selon la clé ; elle ne rend pas automatiquement le contenu secret.

JWT (JSON Web Token, jeton web au format de notation d'objets JavaScript) est un format de jeton. Décoder un jeton n'est pas le valider. Sa validation dépend notamment de l'algorithme attendu, de la clé, de la durée, de l'émetteur et du destinataire prévu. La révocation doit être pensée dans l'architecture. [Spécification du format](https://www.rfc-editor.org/rfc/rfc7519).

## 6. Authentification et délégation

Une personne peut prouver son identité par un secret, un appareil ou d'autres facteurs. Une application peut aussi recevoir une délégation pour agir sur certaines ressources.

OAuth (cadre ouvert de délégation d'autorisation) désigne un cadre de délégation d'autorisation. Il ne doit pas être présenté seul comme un protocole universel d'identité. OpenID Connect ajoute une couche d'identité dans les usages prévus. Les rôles, les redirections et les portées doivent être compris avant intégration. [Cadre d'autorisation](https://www.rfc-editor.org/rfc/rfc6749), [couche d'identité](https://openid.net/specs/openid-connect-core-1_0.html).

Exemple : un outil de calendrier reçoit le droit de lire les disponibilités. Il n'a pas besoin de modifier les comptes de l'organisation. Le jeton de cette intégration doit pouvoir expirer ou être retiré.

Le cas GitHub du cours illustre la valeur de ces autorisations déléguées. Il ne signifie pas que toute délégation soit une faiblesse : la conception des permissions et leur gestion déterminent le risque.

## 7. Chiffrement symétrique et asymétrique

Le chiffrement symétrique utilise un secret partagé pour les opérations prévues. Il est adapté à de nombreux volumes de données, mais impose une bonne gestion des clés.

La cryptographie asymétrique utilise une paire de clés liées. La clé publique peut être diffusée ; la clé privée doit rester protégée. Les opérations possibles dépendent du mécanisme : chiffrement, signature ou échange de clés ne sont pas interchangeables.

Un protocole moderne de transport combine souvent plusieurs mécanismes : authentification, établissement de clés et protection des échanges. Il faut utiliser les bibliothèques et protocoles adaptés plutôt qu'inventer une combinaison artisanale.

<details>
<summary>Comprendre simplement : verrouiller et signer sont deux actions différentes</summary>
<p>Une enveloppe fermée cherche à cacher son contenu. Une signature aide à vérifier qui approuve le contenu et s'il a été modifié. Un document peut être signé sans être secret, et secret sans être correctement attribué.</p>
</details>

## 8. Empreintes, dérivation et intégrité

Une empreinte généraliste aide à comparer un fichier à une référence. SHA-256 (Secure Hash Algorithm 256 bits, algorithme d'empreinte sécurisée sur 256 bits) produit 256 bits de résultat. Il faut encore savoir d'où vient l'empreinte de référence.

Pour les mots de passe, on préfère une fonction de dérivation conçue pour rendre les essais coûteux, avec sel et paramètres adaptés. Une même durée de calcul n'a pas nécessairement le même effet selon le matériel de l'attaquant ; le maintien des paramètres compte.

Le chiffrement de la base de mots de passe peut compléter la défense, mais ne remplace pas la dérivation. Si l'application doit retrouver tous les mots de passe en clair, sa compromission expose un risque différent.

## 9. Le certificat et la confiance

Un certificat associe notamment une clé publique à une identité de service sous des conditions définies. La validation examine la chaîne de confiance, la période de validité et le nom attendu selon le protocole utilisé.

Accepter n'importe quel certificat supprime une partie de la vérification de l'identité du serveur. À l'inverse, un certificat valide ne garantit pas que la logique de l'application soit correcte. Le contrôle de facture reste nécessaire.

Une erreur de certificat ne doit pas être corrigée en demandant aux utilisateurs d'ignorer toutes les alertes. Il faut identifier la cause : mauvais nom, horloge, chaîne manquante ou configuration.

## 10. Capteurs, visibilité et temps

Un journal applicatif voit des identités et des actions que le réseau ne connaît pas toujours. Une capture réseau voit des échanges que l'application peut ne pas journaliser. Un capteur de poste observe des processus et accès locaux. Le croisement augmente la compréhension.

Les horloges doivent être comparables. Un décalage peut donner l'impression que la réponse précède la demande. Noter les fuseaux et la précision des horodatages dans un exercice de reconstitution.

L'absence d'un événement dans un journal ne prouve pas toujours l'absence de l'action : capteur inactif, filtre, rotation ou journal incomplet sont des explications possibles.

## Exercices de transfert

1. Une facture est livrée sous connexion chiffrée à un compte tiers : nommer le contrôle manquant.
2. Un jeton est lisible après décodage : dire ce qu'il faut encore vérifier.
3. Une adresse privée possède une route par défaut : expliquer pourquoi elle peut communiquer à l'extérieur.
4. Un fichier et son empreinte viennent de la même source inconnue : décrire la limite de confiance.
5. Deux journaux semblent contradictoires : proposer une comparaison des temps et des points de collecte.

Retour : [Parcours pédagogique](../02-Semaines/Parcours-pedagogique.md).
