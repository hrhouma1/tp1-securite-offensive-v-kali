---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 16
semaine_associee: 4
duree_minutes_indicative: 40
---

# Laboratoire 16 — Cartographier les ports du laboratoire avec Nmap

## Mission et contexte

Observer le changement de cartographie avant et après le démarrage du service secondaire.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Nmap.
- Mode : Service local requis.
- Lire la [théorie associée à la semaine 4](../../02-Semaines/Semaine-04-Reconnaissance-active-et-cartographie/01-Cours/Reconnaissance-active-et-cartographie-reseau.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 40 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Un scan connect demande au système d’établir des connexions. Nmap interprète les réponses reçues ; un état observé est lié au moment du test. Le nom de service supposé à partir du numéro de port n’est pas une identification certaine.

<details>
<summary>Comprendre simplement</summary>
<p>On vérifie quelles portes répondent, sans déduire automatiquement le métier des personnes derrière chacune.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
nmap -sT -Pn -n -p 8080,8081 --max-retries 1 --host-timeout 20s -oN travail/preuves/lab16-avant.txt 127.0.0.1
# Dans un autre terminal, depuis le même dossier : python3 outils/serveur.py --port 8081
nmap -sT -Pn -n -p 8080,8081 --max-retries 1 --host-timeout 20s -oN travail/preuves/lab16-apres.txt 127.0.0.1
diff travail/preuves/lab16-avant.txt travail/preuves/lab16-apres.txt
```

-sT choisit le scan connect ; -Pn évite une phase de découverte ; -n évite la résolution de noms ; -p borne les ports. Le second test doit être fait après le démarrage indiqué en commentaire.

### 3. Interpréter

8081 change normalement d’état si aucun autre service ne l’occupait. Les deux traces enregistrent aussi l’heure de leur exécution.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Arrêter le service secondaire et vérifier que sa présence ne persiste pas. Ne pas analyser tout le réseau de classe.

## Défi autonome

Expliquer pourquoi un scan local ne démontre pas l’exposition du service depuis une autre machine.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Un état inattendu exige un retour à ss, pas l’ajout d’une plage de cibles.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab16`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Un état inattendu exige un retour à ss, pas l’ajout d’une plage de cibles.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Nmap — techniques de scan](https://nmap.org/book/man-port-scanning-techniques.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
