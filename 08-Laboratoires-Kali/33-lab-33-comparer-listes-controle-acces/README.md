---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 33
semaine_associee: 10
duree_minutes_indicative: 55
---

# Laboratoire 33 — Comprendre les listes de contrôle d’accès Linux et Windows

## Mission et contexte

Observer une permission Linux masquée et repérer un droit excessif dans un document Windows fictif, sans exécuter Windows.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : setfacl, getfacl, Python 3.
- Mode : Linux réel et représentation Windows simulée.
- Lire la [théorie associée à la semaine 10](../../02-Semaines/Semaine-10-Elevation-de-privileges/01-Cours/Identites-permissions-et-elevation-de-privileges.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 55 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

ACL (Access Control List, liste de contrôle d’accès) exprime des permissions supplémentaires. Le masque d’une liste Linux peut limiter les droits effectifs d’une entrée nommée. DACL (Discretionary Access Control List, liste discrétionnaire de contrôle d’accès) est un concept Windows distinct : son modèle ne se transpose pas ligne pour ligne.

<details>
<summary>Comprendre simplement</summary>
<p>Une liste de badges autorisés complète la règle générale de la porte ; un plafond commun peut encore restreindre ce que certains badges permettent.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
cp travail/prive/message.txt travail/copies/lab33-acl.txt
setfacl -m u:nobody:rw- travail/copies/lab33-acl.txt
setfacl -m m::r-- travail/copies/lab33-acl.txt
getfacl travail/copies/lab33-acl.txt
python3 -m json.tool travail/autorisations-windows.json
```

L’entrée nobody est ajoutée à un fichier de démonstration appartenant à l’étudiant ; le masque retire son écriture effective. Aucune connexion avec ce compte n’est nécessaire. Le fichier Windows est une représentation simplifiée, pas une sortie native.

### 3. Interpréter

L’écriture accordée à nobody est marquée inefficace par le masque ; le scénario Windows comporte un accès en écriture trop large.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Retirer l’entrée nobody avec setfacl -x u:nobody sur ce fichier précis et proposer, dans une copie du scénario, l’absence d’écriture pour ToutLeMonde.

## Défi autonome

Expliquer la différence entre permission affichée et permission effective ; présenter les limites de la simulation Windows.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Vérifier l’existence du compte nobody avec getent passwd nobody. Si absent, demander un compte de test autorisé, sans le créer automatiquement.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab33`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Vérifier l’existence du compte nobody avec getent passwd nobody. Si absent, demander un compte de test autorisé, sans le créer automatiquement.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Linux — manuel des listes de contrôle d’accès](https://man7.org/linux/man-pages/man5/acl.5.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
