---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 19
semaine_associee: 4
duree_minutes_indicative: 45
---

# Laboratoire 19 — Reconstituer une requête HTTP dans une capture

## Mission et contexte

Extraire la méthode, le chemin et les statuts de réponse de la capture locale.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : TShark.
- Mode : Lecture de la capture du laboratoire 18. Avoir terminé le laboratoire 18 et conservé sa capture.
- Lire la [théorie associée à la semaine 4](../../02-Semaines/Semaine-04-Reconnaissance-active-et-cartographie/01-Cours/Reconnaissance-active-et-cartographie-reseau.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

HTTP (Hypertext Transfer Protocol, protocole de transfert hypertexte) transporte ici une requête et une réponse non chiffrées. Un filtre d’affichage sélectionne des paquets déjà capturés. Il ne modifie pas le contenu du fichier d’origine.

<details>
<summary>Comprendre simplement</summary>
<p>Après avoir enregistré une conversation autorisée, on sélectionne seulement les phrases contenant une demande précise.</p>
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
tshark -r travail/preuves/lab18-local.pcap -d tcp.port==8080,http -Y http.request -T fields -e frame.number -e http.request.method -e http.request.uri
tshark -r travail/preuves/lab18-local.pcap -d tcp.port==8080,http -Y http.response -T fields -e frame.number -e http.response.code
sha256sum travail/preuves/lab18-local.pcap
```

-r lit le fichier ; -d indique le décodage attendu sur le port 8080 ; -Y applique un filtre d’affichage ; -T fields choisit des colonnes.

### 3. Interpréter

Au moins une requête GET vers /health et son statut de réponse sont identifiés, avec des numéros de trame.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Expliquer pourquoi des identifiants ne doivent pas circuler en HTTP non chiffré en production. Relier cette observation au laboratoire sur TLS.

## Défi autonome

Expliquer la différence entre le filtre tcp port 8080 de la capture et le filtre http.request de lecture.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Si aucun champ n’apparaît, examiner la capture sans filtre avant de conclure à l’absence de trafic.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab19`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Si aucun champ n’apparaît, examiner la capture sans filtre avant de conclure à l’absence de trafic.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Wireshark — manuel de TShark](https://www.wireshark.org/docs/man-pages/tshark.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
