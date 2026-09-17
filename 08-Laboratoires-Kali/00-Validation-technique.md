---
tags: [cours, kali, validation]
maj: 2026-09-17
statut: verifie-partiellement
---

# Vérification technique des 50 laboratoires

## Contrôles réalisés

- 50 énoncés et 50 corrigés présents, avec préparation et ressources communes.
- 106 notes de la banque contrôlées : 617 liens internes aboutissent à un fichier, aucune destination manquante.
- 50 blocs de commandes soumis au contrôle de syntaxe Bash, sans erreur. Cela ne valide pas la syntaxe interne d’un outil interactif comme Metasploit.
- Quatre programmes Python analysés syntaxiquement.
- Cinq tests automatiques du préparateur et du serveur réussis dans Kali : conservation des données existantes, comparaison des requêtes vulnérables/corrigées, autorisation des factures, encodage HTML, connexions et bornes locales.
- Manipulations guidées de **26 ateliers exécutées dans Kali** : 06, 09, 11, 12, 13, 14, 20, 21, 23, 24, 25, 26, 27, 29, 30, 31, 35, 36, 37, 38, 39, 40, 41, 42, 43 et 48.
- Contrôles avant/après observés, dont permissions 666 puis 640, réponses 401 puis 429 pour la limitation, accès à une facture tierce bloqué par 403, graphe accessible puis inaccessible et empreinte de copie modifiée.
- Accents du message fictif préservés grâce à son encodage explicite ; l’adresse extraite ne conserve pas le point de ponctuation final.

Ces tests ont utilisé des données temporaires et des requêtes de boucle locale. Aucun compte réel, équipement tiers ou service cloud n’a été testé. Les sorties pédagogiques des autres ateliers restent des attentes, pas des observations obtenues avec un outil absent.

## Limites et préparation de classe

La distribution Kali disponible est minimale. John the Ripper, Hashcat, Hydra, Nmap, CeWL, Crunch, les outils d’archives et plusieurs autres logiciels spécialisés du catalogue n’y ont pas été détectés. Aucun paquet n’a été installé automatiquement pour cette intervention.

La recherche avec rockyou.txt, les outils spécialisés, Burp graphique, les captures avec TShark, Mosquitto, le serveur de certificat et Metasploit doivent être essayés sur l’image de classe après installation. La présence de tcpdump et d’OpenSSL ne signifie pas que tous leurs ateliers ont été exécutés.

Le test de permissions a été exécuté dans un dossier temporaire du système de fichiers Linux, pas sur le volume Windows monté. Les analyses cloud, Windows, mobile et Wi-Fi restent des simulations documentaires clairement identifiées. Aucune authentification de production, élévation réelle de privilèges ou attaque radio n’est revendiquée.

Les 50 dossiers constituent une banque formative rédigée et partiellement vérifiée en exécution, pas une certification de tous les outils sur toutes les images Kali.

Retour : [Catalogue](00-Index.md).
