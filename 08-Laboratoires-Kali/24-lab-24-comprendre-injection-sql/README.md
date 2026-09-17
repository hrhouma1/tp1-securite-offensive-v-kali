---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 24
semaine_associee: 7
duree_minutes_indicative: 50
---

# Laboratoire 24 — Comparer une requête SQL vulnérable et paramétrée

## Mission et contexte

Faire apparaître le défaut sur les trois produits fictifs en mémoire, puis vérifier le même essai sur la route corrigée.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : curl, SQLite intégré.
- Mode : Service local requis.
- Lire la [théorie associée à la semaine 7](../../02-Semaines/Semaine-07-Securite-des-applications-web/01-Cours/Vulnerabilites-et-protection-des-applications-web.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 50 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

SQL (Structured Query Language, langage de requête structuré) permet d’interroger une base. Concaténer directement une saisie dans une requête peut lui donner un rôle de syntaxe. Une requête paramétrée sépare la structure de l’instruction et les valeurs.

<details>
<summary>Comprendre simplement</summary>
<p>Une donnée écrite sur un formulaire ne doit pas devenir une nouvelle instruction adressée au personnel.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
curl --noproxy '*' -sS -G --data-urlencode 'nom=Casque' http://127.0.0.1:8080/catalogue
curl --noproxy '*' -sS -G --data-urlencode "nom=' OR '1'='1" http://127.0.0.1:8080/catalogue
curl --noproxy '*' -sS -G --data-urlencode "nom=' OR '1'='1" http://127.0.0.1:8080/catalogue-corrige
curl --noproxy '*' -sS -G --data-urlencode 'nom=Casque' http://127.0.0.1:8080/catalogue-corrige
```

-G place les paramètres dans l’adresse et --data-urlencode encode la valeur. La base est recréée en mémoire à chaque test ; elle ne contient aucune donnée réelle.

### 3. Interpréter

La saisie spéciale élargit les résultats uniquement sur la version vulnérable. Le cas légitime reste fonctionnel après correction.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Lire la fonction catalogue du serveur d’origine et expliquer le paramètre ? ainsi que le tuple de valeurs transmis séparément.

## Défi autonome

Ajouter un test automatique négatif et positif sur une copie des tests fournis.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Conserver les apostrophes de la saisie et les guillemets doubles du shell dans la commande fournie.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab24`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Conserver les apostrophes de la saisie et les guillemets doubles du shell dans la commande fournie.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — prévention des injections SQL](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
