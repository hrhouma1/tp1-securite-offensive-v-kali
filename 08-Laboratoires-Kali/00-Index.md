---
tags: [cours, kali, index]
maj: 2026-09-17
statut: proposition-pedagogique
---

# 50 laboratoires sur une seule Kali Linux

Commencer par la [préparation](00-Preparation-Kali.md), puis par le [laboratoire 01 — retrouver un mot de passe avec rockyou.txt](01-lab-01-deviner-mot-de-passe/README.md).

Chaque atelier fournit une mission, une explication vulgarisée, des commandes expliquées, un défi, des indices, des preuves à remettre et une correction à vérifier. Les 50 corrigés sont séparés dans l’espace enseignant.

Une seule machine Kali suffit aux activités proposées. Les services de test écoutent uniquement sur la boucle locale. Les volets Windows, cloud, mobile et Wi-Fi sont des analyses de configurations ou de données **simulées**, pas des validations sur ces plateformes réelles. Aucun compte cloud, téléphone, réseau voisin ou seconde machine n’est requis.

## Parcours conseillés

- Première réussite : préparation, 01, 04, 15, 21 et 26.
- Mots de passe : 01 à 10, puis 22, 23 et 30.
- Reconnaissance et réseau : 11 à 19, puis 35, 44 et 47.
- Applications web : 21 à 30 et 45.
- Systèmes et configurations : 31 à 43 et 48.
- Mission professionnelle : 20, 38, 46, 49 et 50.

Les numéros de laboratoire ne sont pas des numéros de semaine. Leur rattachement à la théorie est une proposition pédagogique. Les durées cumulées représentent **39 h 55**, hors installation et approfondissements : il s’agit d’une banque à sélectionner, pas d’un ajout aux heures officielles du cours.

## Catalogue

| N° | Laboratoire | Semaine | Minutes |
|---:|---|---:|---:|
| 01 | [Retrouver un mot de passe avec rockyou.txt](01-lab-01-deviner-mot-de-passe/README.md) | 10 | 45 |
| 02 | [Comprendre une empreinte de mot de passe Linux](02-lab-02-tester-empreinte-linux/README.md) | 10 | 45 |
| 03 | [Construire un dictionnaire à partir d’un site fictif](03-lab-03-construire-dictionnaire-contexte/README.md) | 3 | 45 |
| 04 | [Retrouver un code de quatre chiffres](04-lab-04-retrouver-code-quatre-chiffres/README.md) | 10 | 40 |
| 05 | [Montrer les limites de la majuscule et du chiffre final](05-lab-05-tester-regles-mots-de-passe/README.md) | 10 | 45 |
| 06 | [Comparer deux sels pour un même mot de passe](06-lab-06-comprendre-sel-cryptographique/README.md) | 10 | 35 |
| 07 | [Récupérer une archive ZIP pédagogique](07-lab-07-recuperer-archive-zip/README.md) | 10 | 55 |
| 08 | [Protéger un fichier et tester une mauvaise clé](08-lab-08-chiffrer-et-verifier-fichier/README.md) | 10 | 45 |
| 09 | [Mesurer le coût d’une fonction de dérivation](09-lab-09-mesurer-cout-mot-de-passe/README.md) | 10 | 40 |
| 10 | [Concevoir une politique de mots de passe défendable](10-lab-10-auditer-politique-mots-de-passe/README.md) | 2 | 40 |
| 11 | [Bloquer une cible hors du mandat](11-lab-11-definir-perimetre-autorise/README.md) | 2 | 35 |
| 12 | [Mener une reconnaissance passive sur un dossier fictif](12-lab-12-enqueter-sources-locales/README.md) | 3 | 40 |
| 13 | [Déjouer un courriel d’hameçonnage fictif](13-lab-13-detecter-hameconnage/README.md) | 6 | 40 |
| 14 | [Cartographier une zone DNS sans interroger Internet](14-lab-14-lire-zone-dns/README.md) | 3 | 40 |
| 15 | [Associer un port à son processus](15-lab-15-identifier-services-locaux/README.md) | 4 | 35 |
| 16 | [Cartographier les ports du laboratoire avec Nmap](16-lab-16-cartographier-ports-nmap/README.md) | 4 | 40 |
| 17 | [Distinguer bannière et vulnérabilité](17-lab-17-verifier-bannieres-services/README.md) | 5 | 40 |
| 18 | [Capturer uniquement le trafic de son application](18-lab-18-capturer-trafic-local/README.md) | 4 | 45 |
| 19 | [Reconstituer une requête HTTP dans une capture](19-lab-19-analyser-capture-http/README.md) | 4 | 45 |
| 20 | [Prioriser trois constats sans inventer de risque](20-lab-20-prioriser-vulnerabilites/README.md) | 5 | 45 |
| 21 | [Lire une requête et une réponse HTTP](21-lab-21-comprendre-requete-http/README.md) | 7 | 35 |
| 22 | [Tester un formulaire fictif avec Hydra](22-lab-22-tester-connexion-hydra/README.md) | 7 | 50 |
| 23 | [Observer une limitation des tentatives](23-lab-23-limiter-tentatives-connexion/README.md) | 7 | 35 |
| 24 | [Comparer une requête SQL vulnérable et paramétrée](24-lab-24-comprendre-injection-sql/README.md) | 7 | 50 |
| 25 | [Tester l’injection HTML et comprendre le risque XSS](25-lab-25-comprendre-injection-html/README.md) | 7 | 45 |
| 26 | [Empêcher l’accès à la facture d’un autre client](26-lab-26-verifier-acces-factures/README.md) | 7 | 45 |
| 27 | [Bloquer une traversée de répertoires](27-lab-27-bloquer-traversee-repertoires/README.md) | 7 | 45 |
| 28 | [Observer et rejouer une requête avec Burp Suite](28-lab-28-observer-requete-burp/README.md) | 7 | 55 |
| 29 | [Repérer une injection de commandes avant exécution](29-lab-29-reperer-injection-commandes/README.md) | 14 | 45 |
| 30 | [Comprendre les cookies de session et leurs limites](30-lab-30-comprendre-cookies-session/README.md) | 7 | 45 |
| 31 | [Corriger un fichier modifiable par tout le monde](31-lab-31-corriger-permissions-linux/README.md) | 10 | 40 |
| 32 | [Auditer les programmes SUID sans obtenir root](32-lab-32-auditer-programmes-suid/README.md) | 10 | 45 |
| 33 | [Comprendre les listes de contrôle d’accès Linux et Windows](33-lab-33-comparer-listes-controle-acces/README.md) | 10 | 55 |
| 34 | [Détecter une tâche privilégiée dépendant d’un fichier modifiable](34-lab-34-auditer-tache-planifiee/README.md) | 10 | 40 |
| 35 | [Couper un chemin de mouvement latéral dans un modèle](35-lab-35-couper-chemin-mouvement-lateral/README.md) | 11 | 50 |
| 36 | [Détecter un export inhabituel dans des traces](36-lab-36-detecter-export-anormal/README.md) | 11 | 45 |
| 37 | [Reconstituer une chronologie sans inventer l’attaquant](37-lab-37-reconstruire-chronologie-incident/README.md) | 11 | 45 |
| 38 | [Détecter une modification de preuve](38-lab-38-preserver-integrite-preuves/README.md) | 13 | 40 |
| 39 | [Repérer des secrets fictifs et des choix cryptographiques faibles](39-lab-39-detecter-secrets-dans-code/README.md) | 14 | 45 |
| 40 | [Réduire les permissions d’une politique cloud](40-lab-40-reduire-permissions-cloud/README.md) | 12 | 50 |
| 41 | [Distinguer chiffrement et exposition d’un stockage cloud](41-lab-41-auditer-stockage-cloud/README.md) | 12 | 40 |
| 42 | [Auditer une recette de conteneur sans l’exécuter](42-lab-42-auditer-conteneur-sans-docker/README.md) | 12 | 45 |
| 43 | [Auditer les permissions d’une application mobile fictive](43-lab-43-auditer-application-mobile/README.md) | 12 | 45 |
| 44 | [Observer la messagerie d’un objet connecté fictif](44-lab-44-tester-messagerie-objet-connecte/README.md) | 12 | 60 |
| 45 | [Créer et vérifier un certificat local](45-lab-45-verifier-certificat-tls/README.md) | 7 | 60 |
| 46 | [Automatiser un contrôle de sécurité et sa régression](46-lab-46-automatiser-tests-regression/README.md) | 9 | 60 |
| 47 | [Utiliser un module de reconnaissance Metasploit](47-lab-47-decouvrir-metasploit-sans-exploit/README.md) | 9 | 55 |
| 48 | [Auditer une configuration Wi-Fi sans carte radio](48-lab-48-auditer-securite-wifi/README.md) | 12 | 45 |
| 49 | [Transformer une découverte en rapport exploitable](49-lab-49-rediger-rapport-professionnel/README.md) | 13 | 60 |
| 50 | [Mission finale — auditer et sécuriser Atelier Boréal](50-lab-50-mission-finale-atelier-boreal/README.md) | 15 | 180 |

## Ressources communes

- [Préparation et démarrage du portail local](00-Preparation-Kali.md).
- [Progression et barème formatif](00-Evaluation-et-progression.md).
- [Sources et limites de couverture](00-Sources-et-limites.md).
- [État des vérifications techniques](00-Validation-technique.md).
- [Parcours théorique](../02-Semaines/Parcours-pedagogique.md).

Les liens Markdown relatifs sont compatibles avec Obsidian et GitHub. Les accents, les explications dépliables et les termes développés sont conservés.

Retour : [Accueil du cours](../00-Accueil.md).
