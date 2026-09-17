---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 43
semaine_associee: 12
duree_minutes_indicative: 45
---

# Laboratoire 43 — Auditer les permissions d’une application mobile fictive

## Mission et contexte

Repérer les réglages qui dépassent le besoin d’une application de consultation de catalogue.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3, XML.
- Mode : Analyse de manifeste — aucun téléphone requis.
- Lire la [théorie associée à la semaine 12](../../02-Semaines/Semaine-12-Securite-cloud-mobile-et-objets-connectes/01-Cours/Securite-du-cloud-du-mobile-et-des-objets-connectes.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

Un manifeste Android décrit notamment des permissions et des composants. XML (Extensible Markup Language, langage de balisage extensible) encode ce document. Un composant exporté n’est pas automatiquement vulnérable ; il faut examiner son usage, ses autorisations et les données qu’il traite.

<details>
<summary>Comprendre simplement</summary>
<p>Le plan d’un bâtiment indique des portes et leurs règles ; il ne montre pas tout le comportement des personnes à l’intérieur.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
python3 - <<'PY'
import xml.etree.ElementTree as ET
racine = ET.parse("travail/AndroidManifest.xml").getroot()
for element in racine.iter():
    print(element.tag, element.attrib)
PY
cp travail/AndroidManifest.xml travail/copies/lab43-manifeste.xml
```

Le fichier est un extrait XML lisible, pas un APK (Android Package, paquet d’application Android) compilé. Aucun programme Android n’est exécuté.

### 3. Interpréter

La permission de contacts, le débogage et le trafic en clair sont discutés séparément du composant exporté.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Proposer une version de production sans accès aux contacts non justifié, avec débogage désactivé et politique réseau adaptée. Vérifier que la copie reste un XML valide.

## Défi autonome

Écrire deux questions à poser au développeur avant de classer la sévérité.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>La nécessité d’exporter l’activité doit être examinée selon son rôle ; ne pas appliquer une règle aveugle.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab43`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

La nécessité d’exporter l’activité doit être examinée selon son rôle ; ne pas appliquer une règle aveugle.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [Android — manifeste de l’application](https://developer.android.com/guide/topics/manifest/application-element).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
