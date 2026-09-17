---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 4
semaine_associee: 10
duree_minutes_indicative: 40
---

# Laboratoire 04 — Retrouver un code de quatre chiffres

## Mission et contexte

Ouvrir le cadenas numérique fictif en justifiant à l’avance le nombre de candidats.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Crunch, John the Ripper, Hashcat en option.
- Mode : Manipulation hors ligne.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 40 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une recherche exhaustive parcourt toutes les valeurs d’un espace fini. Un code de quatre chiffres, zéros initiaux compris, possède 10 puissance 4 possibilités. Un masque décrit la forme des candidats ; il ne garantit pas que l’hypothèse de forme est correcte.

<details>
<summary>Comprendre simplement</summary>
<p>Un cadenas à quatre molettes possède dix positions par molette. On compte les combinaisons avant de commencer à tourner.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
crunch 4 4 0123456789 -o travail/preuves/lab04-codes.txt
wc -l travail/preuves/lab04-codes.txt
john --format=raw-md5 --wordlist=travail/preuves/lab04-codes.txt --pot=travail/preuves/lab04.pot travail/hashes/04-code.txt
john --show --format=raw-md5 --pot=travail/preuves/lab04.pot travail/hashes/04-code.txt
```

Crunch produit exactement quatre caractères parmi dix chiffres. La limite à quatre positions maintient l’exercice court ; ne pas agrandir aveuglément l’espace de recherche.

### 3. Interpréter

10 000 candidats sont générés et le code conserve son éventuel zéro initial.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Comparer 4 et 8 positions par un calcul seulement, sans générer la grande liste. Expliquer pourquoi une limitation des essais protège un service en ligne mais pas une empreinte déjà copiée.

## Défi autonome

Si Hashcat dispose d’un moteur de calcul : hashcat -m 0 -a 3 --potfile-path travail/preuves/lab04-hashcat.pot travail/hashes/04-code.txt '?d?d?d?d'. Aucun usage de --force.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Traiter le résultat comme une chaîne de caractères, pas comme un entier.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab04`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Traiter le résultat comme une chaîne de caractères, pas comme un entier.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Crunch — Kali](https://www.kali.org/tools/crunch/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
