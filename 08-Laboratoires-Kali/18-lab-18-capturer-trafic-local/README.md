---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 18
semaine_associee: 4
duree_minutes_indicative: 45
---

# Laboratoire 18 — Capturer uniquement le trafic de son application

## Mission et contexte

Produire une capture courte d’une seule consultation du service local.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : tcpdump, curl.
- Mode : Capture réelle de boucle locale.
- Lire la [théorie associée à la semaine 4](../../02-Semaines/Semaine-04-Reconnaissance-active-et-cartographie/01-Cours/Reconnaissance-active-et-cartographie-reseau.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une capture conserve des paquets observés sur une interface. PCAP (Packet Capture, capture de paquets) désigne ici le format de fichier utilisé. Un filtre de capture réduit ce qui est enregistré dès la collecte ; il ne faut pas capturer les échanges des autres étudiants.

<details>
<summary>Comprendre simplement</summary>
<p>Le microphone est posé uniquement devant le guichet d’exercice, pas au milieu de toute la classe.</p>
</details>

## Vocabulaire utile

- TCP (Transmission Control Protocol, protocole de contrôle de transmission).

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
# Terminal A : attendre l'annonce de l'écoute.
sudo tcpdump -i lo -nn -s 0 -U -w travail/preuves/lab18-local.pcap 'tcp port 8080'
# Terminal B :
curl --noproxy '*' --max-time 3 http://127.0.0.1:8080/health
# Revenir au terminal A et arrêter avec Ctrl+C.
# Puis, dans le terminal B :
tcpdump -nn -r travail/preuves/lab18-local.pcap
```

lo est l’interface de boucle locale. -nn évite les résolutions de noms et de services ; -s 0 garde les paquets complets ; -U facilite l’écriture progressive. sudo est limité à la capture.

### 3. Interpréter

Une capture non vide montre uniquement des échanges TCP liés au port 8080 sur la boucle locale.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Vérifier le filtre utilisé et les adresses capturées ; documenter la minimisation de données. Ne pas téléverser la capture vers un service public.

## Défi autonome

Comparer la taille du fichier pour une consultation et pour trois consultations, sans générer de charge importante.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Si la capture est vide, vérifier l’ordre de démarrage et refaire une requête avant Ctrl+C. En cas de permission de lecture, utiliser sudo tcpdump -r sur ce fichier précis.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab18`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Si la capture est vide, vérifier l’ordre de démarrage et refaire une requête avant Ctrl+C. En cas de permission de lecture, utiliser sudo tcpdump -r sur ce fichier précis.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Wireshark — manuel de TShark](https://www.wireshark.org/docs/man-pages/tshark.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
