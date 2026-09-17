---
tags: [cours, ressources, navigation, obsidian, github]
maj: 2026-09-14
statut: rédigé
---

# Lire et relier les notes dans Obsidian et sur GitHub

Les notes du cours partagent un seul format de liens : un intitulé lisible, suivi d’un chemin relatif au fichier qui contient le lien. Il n’est pas nécessaire de conserver deux versions du cours.

## Lire le cours

- Dans Obsidian, ouvrir le dossier du cours comme coffre, puis consulter [l’accueil](../00-Accueil.md) ou [le parcours pédagogique](../02-Semaines/Parcours-pedagogique.md).
- Sur GitHub, commencer par [la page d’accueil du dépôt](../README.md), puis suivre les liens des chapitres et ateliers.
- En mode source, la syntaxe des liens reste visible : c’est normal. Passer en mode lecture pour afficher les intitulés cliquables.

Obsidian reconnaît le format Markdown comme un format de lien interne, au même titre que ses liens entre doubles crochets. La documentation explique ces deux formats et les caractères à encoder dans les chemins. [Source : liens internes dans Obsidian](https://help.obsidian.md/links).

## Exemple concret : l’atelier de la semaine 4

Dans la note de laboratoire, le chapitre théorique se trouve dans le dossier voisin `01-Cours/`. Le lien s’écrit :

```markdown
[Chapitre théorique](../01-Cours/Reconnaissance-active-et-cartographie-reseau.md)
```

Le texte affiché est seulement « Chapitre théorique ». Le début `../` remonte du dossier du laboratoire vers celui de la semaine ; la suite ouvre le chapitre. Depuis une autre note, le chemin peut être différent, car il dépend de l’emplacement de départ.

Ouvrir [l’atelier de la semaine 4](../02-Semaines/Semaine-04-Reconnaissance-active-et-cartographie/02-Laboratoire/Atelier-Reconnaissance-active-et-cartographie-reseau.md) pour voir ce principe en situation.

GitHub calcule également les liens relatifs à partir du fichier affiché, ce qui permet de conserver la navigation dans une copie locale du dépôt. [Source : liens relatifs sur GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#relative-links).

## Créer de nouveaux liens dans Obsidian

Les liens déjà présents fonctionnent sans modifier les réglages. Pour qu’Obsidian crée les prochains liens dans le même format, les préférences utiles sont dans **Paramètres → Fichiers et liens** :

1. Désactiver l’option de génération des liens entre doubles crochets, nommée *Use Wikilinks* dans l’interface anglaise.
2. Choisir **Chemin relatif au fichier** pour le format des nouveaux liens.
3. Activer la mise à jour automatique des liens internes lors d’un changement de nom, si ce comportement est souhaité.

Ces réglages sont des préférences locales ; ils n’ont pas été modifiés par cette correction. Obsidian documente les formats relatifs et la mise à jour des liens dans ses paramètres. [Source : réglages des fichiers et liens](https://help.obsidian.md/settings).

## Préserver la compatibilité

- Conserver une extension explicite : `.md` pour une note, ou l’extension réelle d’une pièce jointe.
- Respecter exactement les majuscules et minuscules des noms de fichiers.
- Utiliser `/` dans les chemins, y compris sous Windows.
- Encoder un espace dans un chemin avec `%20` ; conserver les accents dans les titres et dans les textes affichés.
- Après un déplacement ou un renommage, vérifier les liens entrants et les liens sortants avant de publier.
- Garder les propriétés des notes en début de fichier et laisser les réglages personnels hors du dépôt.

Les fichiers de données ne sont pas des notes : les [données synthétiques de l’atelier](Atelier-Boreal/donnees-observation.json) utilisent JSON (JavaScript Object Notation, format texte de représentation de données). Leur ouverture peut utiliser une application externe si Obsidian ne les affiche pas directement.

## Explications dépliables

Les blocs `<details>` et `<summary>` du cours sont conservés. Cliquer sur leur intitulé pour afficher l’explication ; en mode source, les balises restent visibles.

Lors d’un ajout, garder une ligne vide autour du contenu Markdown à l’intérieur du bloc. GitHub documente cette structure pour les sections dépliables. [Source : sections dépliables sur GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections).

Retour : [Ressources du cours](00-Index.md) · [Guide de lecture](../00-Lire-le-cours.md).
