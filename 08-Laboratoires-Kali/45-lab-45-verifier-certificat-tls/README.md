---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 45
semaine_associee: 7
duree_minutes_indicative: 60
---

# Laboratoire 45 — Créer et vérifier un certificat local

## Mission et contexte

Créer un certificat de laboratoire, observer le refus par défaut puis établir une confiance explicite limitée à ce certificat.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : OpenSSL, curl.
- Mode : Service TLS local temporaire.
- Lire la [théorie associée à la semaine 7](../../02-Semaines/Semaine-07-Securite-des-applications-web/01-Cours/Vulnerabilites-et-protection-des-applications-web.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 60 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

TLS (Transport Layer Security, sécurité de la couche de transport) protège un canal et participe à l’authentification du serveur. Un certificat auto-signé ne devient pas universellement fiable parce qu’il chiffre le trafic. Le client doit vérifier une chaîne de confiance et l’identité du serveur.

<details>
<summary>Comprendre simplement</summary>
<p>Le colis peut être scellé et remis à la mauvaise personne si l’identité du destinataire n’est pas vérifiée.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
openssl req -x509 -newkey rsa:2048 -nodes -days 2 -keyout travail/copies/lab45-cle.pem -out travail/copies/lab45-cert.pem -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost,IP:127.0.0.1'
chmod 600 travail/copies/lab45-cle.pem
# Terminal A :
openssl s_server -accept 127.0.0.1:8443 -cert travail/copies/lab45-cert.pem -key travail/copies/lab45-cle.pem -www
# Terminal B :
curl --noproxy '*' --max-time 3 https://127.0.0.1:8443/
curl --noproxy '*' --max-time 3 --cacert travail/copies/lab45-cert.pem https://127.0.0.1:8443/
```

RSA (Rivest–Shamir–Adleman, algorithme à clé publique) sert ici à créer une clé de test. SAN (Subject Alternative Name, nom alternatif du sujet) indique les identités du serveur. -nodes crée une clé privée non chiffrée uniquement pour ce laboratoire.

### 3. Interpréter

La première connexion refuse normalement le certificat auto-signé ; la seconde réussit avec une confiance explicitement fournie et une identité correspondant à 127.0.0.1.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Expliquer pourquoi --insecure n’est pas une correction. Ne pas importer ce certificat dans le magasin de confiance global.

## Défi autonome

Inspecter les dates et noms avec openssl x509 -in travail/copies/lab45-cert.pem -noout -text, sans publier la clé privée.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Lancer s_server dans un terminal séparé et l’arrêter avec Ctrl+C avant de ranger les fichiers.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab45`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Lancer s_server dans un terminal séparé et l’arrêter avec Ctrl+C avant de ranger les fichiers.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OpenSSL — serveur TLS de test](https://docs.openssl.org/master/man1/openssl-s_server/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
