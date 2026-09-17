---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 1
semaine_associee: 10
duree_minutes_indicative: 45
---

# Laboratoire 01 — Retrouver un mot de passe avec rockyou.txt

## Mission et contexte

Une ancienne application fictive a conservé une empreinte sans sel. Retrouver le mot de passe du compte de démonstration et expliquer la faiblesse de stockage.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : John the Ripper, rockyou.txt, md5sum.
- Mode : Manipulation hors ligne.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Une attaque par dictionnaire calcule l’empreinte de chaque candidat et la compare à l’empreinte fournie. Elle ne déchiffre pas le hachage : elle retrouve une entrée qui produit le même résultat. MD5 (Message Digest 5, fonction d’empreinte de 128 bits) est ici volontairement inadapté au stockage des mots de passe.

<details>
<summary>Comprendre simplement</summary>
<p>On essaie les clés d’un trousseau déjà constitué. Une clé absente du trousseau ne sera pas trouvée, même avec un ordinateur rapide.</p>
</details>

## Vocabulaire utile

- SHA-256 (Secure Hash Algorithm 256, algorithme d’empreinte de 256 bits).

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
john --format=raw-md5 --wordlist=travail/rockyou.txt --pot=travail/preuves/lab01.pot travail/hashes/01-md5.txt
john --show --format=raw-md5 --pot=travail/preuves/lab01.pot travail/hashes/01-md5.txt
printf '%s' 'CANDIDAT_RETROUVE' | md5sum
```

--format fixe le format connu de la donnée ; --wordlist désigne les candidats ; --pot isole les résultats de cet atelier. Remplacer CANDIDAT_RETROUVE par la réponse observée, sans ajouter de retour à la ligne dans le calcul.

### 3. Interpréter

Une correspondance est retrouvée, puis son empreinte est recalculée indépendamment. Aucun compte réel et aucun service réseau ne sont interrogés.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Rédiger une recommandation de stockage avec une fonction dédiée aux mots de passe et un sel unique. Ne pas proposer de remplacer simplement MD5 par SHA-256.

## Défi autonome

Refaire le test avec une copie du dictionnaire dont le candidat a été retiré : conclure seulement que la liste testée ne contient pas la réponse.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Le fichier contient une empreinte MD5 brute, pas une ligne issue de /etc/shadow. Le dictionnaire rockyou.txt doit être extrait à la préparation.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab01`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Le fichier contient une empreinte MD5 brute, pas une ligne issue de /etc/shadow. Le dictionnaire rockyou.txt doit être extrait à la préparation.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [John the Ripper — Kali](https://www.kali.org/tools/john/).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
