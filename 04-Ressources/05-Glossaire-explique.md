---
tags: [cours, glossaire, vocabulaire]
maj: 2026-09-13
---
# Glossaire expliqué de la sécurité offensive

Chaque définition associe le mot à son usage dans le cours. Les noms de produits, comme Kali, Nmap ou Wireshark, restent des noms de produits.

## Actif

Élément qui a de la valeur pour l'organisation : service de réservation, facture ou compte. La sensibilité dépend de l'usage.

## Vulnérabilité

Faiblesse qui permet de dépasser une règle de sécurité dans certaines conditions. Une alerte est seulement une piste tant que son application reste incertaine.

## Menace

Cause possible d'un dommage. Elle peut être humaine, technique ou accidentelle.

## Risque

Possibilité d'un événement et gravité de ses conséquences dans un contexte donné. Ce n'est pas uniquement un score de logiciel.

## Exposition

Conditions dans lesquelles un actif ou un service est accessible. On précise depuis où, par qui et à quel moment.

## Pentest (Penetration Test, test d'intrusion)

Mission autorisée qui vérifie des possibilités de franchissement de sécurité et fournit des recommandations.

## RoE (Rules of Engagement, règles d'engagement)

Document qui définit comment la mission se déroule : cibles, actions, horaires, contacts et arrêt.

## OSINT (Open Source Intelligence, renseignement à partir de sources ouvertes)

Analyse de sources accessibles afin de répondre à une question. Une donnée trouvée doit être datée et recoupée.

## VM (Virtual Machine, machine virtuelle)

Ordinateur simulé par un hyperviseur. Le système invité est distinct de l'hôte, sans être automatiquement parfaitement isolé.

## Hyperviseur

Logiciel qui répartit les ressources de l'hôte entre des systèmes invités.

## Instantané

État enregistré permettant un retour de travail. Il ne remplace pas une sauvegarde indépendante.

## IP (Internet Protocol, protocole Internet)

Protocole d'adressage et d'acheminement. Une adresse sert à identifier un point de communication, pas une personne certaine.

## TCP (Transmission Control Protocol, protocole de contrôle de transmission)

Transport avec état, livraison ordonnée et retransmission. Un service peut accepter une connexion puis refuser une action.

## UDP (User Datagram Protocol, protocole de datagramme utilisateur)

Transport de messages sans la session fiable du protocole précédent. Le silence y est souvent ambigu.

## DNS (Domain Name System, système de noms de domaine)

Système distribué associant les noms à plusieurs types d'informations, dont des adresses.

## NAT (Network Address Translation, traduction d'adresses réseau)

Modification d'adresses entre réseaux ; utile pour certains accès, mais pas synonyme d'isolation.

## VLAN (Virtual Local Area Network, réseau local virtuel)

Séparation logique de réseau local. Les règles interzones complètent la segmentation.

## HTTP (Hypertext Transfer Protocol, protocole de transfert hypertexte)

Protocole d'échange de requêtes et réponses utilisé par les applications web.

## HTTPS (Hypertext Transfer Protocol Secure, protocole de transfert hypertexte sécurisé)

Échanges web protégés par un canal chiffré et authentifié. Le contrôle d'accès reste nécessaire.

## TLS (Transport Layer Security, sécurité de la couche de transport)

Protocole établissant un canal protégé, généralement avec un certificat côté serveur.

## SSL (Secure Sockets Layer, ancienne famille de protocoles de sécurisation)

Terme historique encore utilisé dans le langage courant ; ne pas le confondre avec les versions modernes du transport sécurisé.

## SSH (Secure Shell, protocole d'accès distant sécurisé)

Protocole d'administration distante et de transport chiffré. Son autorisation dépend des comptes et de la configuration.

## SMB (Server Message Block, protocole de partage de fichiers et de ressources)

Protocole courant de partage. Voir un partage, le lire et y écrire sont trois observations différentes.

## SQL (Structured Query Language, langage de requête structuré)

Langage d'interrogation des bases relationnelles. Les valeurs reçues doivent rester distinctes de l'instruction.

## XSS (Cross-Site Scripting, injection de script dans une page web)

Interprétation de contenu non fiable comme code dans le navigateur. Le contexte détermine la défense.

## CSRF (Cross-Site Request Forgery, falsification de requête intersites)

Action provoquée avec des informations de session envoyées automatiquement par le navigateur.

## SSRF (Server-Side Request Forgery, falsification de requête côté serveur)

Utilisation détournée d'un serveur pour contacter une destination non prévue.

## IDOR (Insecure Direct Object Reference, référence directe non sécurisée à un objet)

Accès à un objet par son identifiant sans contrôle suffisant des permissions.

## API (Application Programming Interface, interface de programmation applicative)

Contrat d'échange entre programmes. Elle doit appliquer ses propres contrôles côté serveur.

## HTML (HyperText Markup Language, langage de balisage hypertexte)

Langage structurant les pages. Les blocs details et summary de ce cours créent des explications dépliables.

## URL (Uniform Resource Locator, adresse d'une ressource)

Adresse comprenant notamment protocole, nom, chemin et paramètres. Les différentes parties n'ont pas le même rôle.

## JSON (JavaScript Object Notation, notation d'objets JavaScript)

Format de données textuelles structuré. Il ne prouve pas la validité métier de son contenu.

## CSV (Comma-Separated Values, valeurs séparées par des virgules)

Format tabulaire textuel. Le séparateur réel peut varier selon les outils et paramètres régionaux.

## CVE (Common Vulnerabilities and Exposures, identifiants communs de vulnérabilités et d'expositions)

Référence d'une vulnérabilité publiée. Son numéro ne prouve pas l'exposition de notre installation.

## CWE (Common Weakness Enumeration, classification commune des faiblesses)

Classification des types de défauts, utile pour comprendre les causes récurrentes.

## NVD (National Vulnerability Database, base nationale américaine des vulnérabilités)

Base d'informations enrichies sur les vulnérabilités connues.

## CVSS (Common Vulnerability Scoring System, système commun de notation des vulnérabilités)

Système de description de la sévérité technique ; la version et le vecteur accompagnent le score.

## EPSS (Exploit Prediction Scoring System, système de prédiction de l'exploitation)

Estimation d'exploitation dans la nature à trente jours ; pas un diagnostic de notre serveur.

## PoC (Proof of Concept, preuve de concept)

Démonstration d'une possibilité. Elle peut avoir des effets ou dépendances qui doivent être examinés.

## MFA (Multi-Factor Authentication, authentification multifacteur)

Vérification faisant intervenir des catégories de facteurs distinctes.

## ACL (Access Control List, liste de contrôle d'accès)

Règles indiquant quelles identités ont quels droits sur un objet.

## IAM (Identity and Access Management, gestion des identités et des accès)

Organisation des identités, actions, ressources et conditions d'autorisation.

## IaaS (Infrastructure as a Service, infrastructure en tant que service)

Fourniture de ressources d'infrastructure ; le client conserve notamment la responsabilité de ses systèmes invités.

## PaaS (Platform as a Service, plateforme en tant que service)

Fourniture d'un environnement d'exécution administré, avec des responsabilités client persistantes.

## SaaS (Software as a Service, logiciel en tant que service)

Application fournie comme service ; comptes, données et permissions client restent à gérer.

## IoT (Internet of Things, Internet des objets)

Équipements connectés ayant logiciel, identités, services et cycle de vie.

## EDR (Endpoint Detection and Response, détection et réponse sur les postes)

Fonctions d'observation et de réponse sur les terminaux selon la couverture du produit.

## DLP (Data Loss Prevention, prévention des fuites de données)

Contrôles destinés à identifier ou limiter certaines sorties de données sensibles.

## Hachage

Calcul d'une empreinte sans opération inverse prévue. Pour les mots de passe, utiliser une dérivation adaptée et un sel.

## Sel

Valeur distincte associée à une entrée de mot de passe pour éviter des résultats identiques entre entrées. Elle n'a généralement pas besoin d'être secrète.

## Chiffrement

Transformation réversible avec une clé appropriée. La gestion de cette clé fait partie de la protection.

## Jeton

Valeur représentant un contexte d'accès ou une autorisation. Sa portée, sa durée et sa révocation sont essentielles.

## Session

Contexte qui relie plusieurs échanges à une identité et à un état. Elle doit pouvoir être expirée et retirée.

## Moindre privilège

Attribution des seuls droits nécessaires à la fonction et à la durée du besoin.

## Faux positif

Alerte qui ne correspond pas à la condition recherchée. Une absence de reproduction ne suffit pas toujours à conclure.

## Faux négatif

Condition présente que la méthode n'a pas détectée. On ne le mesure pas en regardant seulement les alertes produites.

## Remédiation

Ensemble des actions qui corrigent une faiblesse ou réduisent ses conséquences. La nouvelle vérification confirme leur effet.

<details>
<summary>Comprendre simplement : savoir développer un sigle ne suffit pas</summary>
<p>Pour chaque terme, donner une phrase de fonctionnement et un exemple. « Authentification : reconnaître Alice ; autorisation : décider si Alice peut lire cette facture. » Cet exemple montre la distinction mieux qu'une liste de mots anglais.</p>
</details>

Retour : [Lire le cours](../00-Lire-le-cours.md).
