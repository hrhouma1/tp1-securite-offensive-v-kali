---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 8
semaine_associee: 10
duree_minutes_indicative: 45
---

# Laboratoire 08 — Protéger un fichier et tester une mauvaise clé

## Mission et contexte

Protéger le message fictif et démontrer séparément le refus d’une mauvaise phrase puis la récupération intacte.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : GnuPG, sha256sum.
- Mode : Manipulation hors ligne.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

GnuPG réalise ici un chiffrement symétrique : la même phrase secrète permet de chiffrer et de déchiffrer. Une empreinte du fichier original sert ensuite à vérifier que la récupération est exacte. Le chiffrement ne corrige pas un secret faible ou partagé sans contrôle.

<details>
<summary>Comprendre simplement</summary>
<p>Le cadenas protège le colis ; le reçu signé de son contenu permet de vérifier que le bon colis a été récupéré.</p>
</details>

## Vocabulaire utile

- GnuPG (GNU Privacy Guard, outil de chiffrement et de signature).

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
mkdir -p travail/gnupg
chmod 700 travail/gnupg
gpg --homedir travail/gnupg --no-symkey-cache --symmetric --cipher-algo AES256 --output travail/copies/lab08-message.gpg travail/prive/message.txt
gpg --homedir travail/gnupg --no-symkey-cache --output travail/copies/lab08-recupere.txt --decrypt travail/copies/lab08-message.gpg
sha256sum travail/prive/message.txt travail/copies/lab08-recupere.txt
```

Saisir une phrase fictive dans la fenêtre ou le terminal de GnuPG, pas dans la commande. AES (Advanced Encryption Standard, norme de chiffrement avancé) est utilisé ici avec une clé de 256 bits. --no-symkey-cache évite de confondre un secret mémorisé avec un nouveau test.

### 3. Interpréter

Après un essai négatif puis un essai correct, les deux empreintes du contenu correspondent. Ne pas écraser un résultat existant lors d’une reprise.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Expliquer où conserver une phrase secrète et pourquoi envoyer le fichier et sa clé dans le même message réduit l’intérêt de la protection.

## Défi autonome

Faire expliquer par le binôme la différence entre chiffrement, hachage et encodage.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Si une sortie partielle existe après un échec, choisir un nouveau nom de sortie avant de relancer.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab08`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Si une sortie partielle existe après un échec, choisir un nouveau nom de sortie avant de relancer.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [GnuPG — commandes](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Commands.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
