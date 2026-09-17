---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 39
semaine_associee: 14
duree_minutes_indicative: 45
---

# Laboratoire 39 — Repérer des secrets fictifs et des choix cryptographiques faibles

## Mission et contexte

Classer les alertes du code fourni et proposer des corrections distinctes pour secret embarqué et stockage de mot de passe.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : grep, Python 3.
- Mode : Analyse statique — aucun échantillon exécuté.
- Lire la [théorie associée à la semaine 14](../../02-Semaines/Semaine-14-Analyse-de-code-et-outils/01-Cours/Analyse-de-code-et-securite-des-outils.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 45 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

La recherche de secrets dans le code détecte des motifs à examiner. Un mot nommé SECRET peut être un exemple sans valeur, tandis qu’un secret réel peut porter un nom banal. Une détection n’autorise jamais à tester un identifiant découvert contre un service.

<details>
<summary>Comprendre simplement</summary>
<p>Une inspection repère les étiquettes « clé » dans les tiroirs ; il faut encore déterminer ce que l’objet est, sans essayer toutes les portes.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
grep -nEi 'secret|password|md5|shell=True' travail/code-a-auditer.txt travail/Dockerfile.exemple
sha256sum travail/code-a-auditer.txt
cp travail/code-a-auditer.txt travail/copies/lab39-proposition.txt
```

Les valeurs portent explicitement la mention faux ou exemple. Le fichier de code n’est pas lancé ; aucune clé n’est utilisée sur Internet.

### 3. Interpréter

Chaque alerte est qualifiée : donnée fictive, construction risquée ou élément à contextualiser.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Annoter la copie avec une source de secret adaptée à l’exécution et une fonction dédiée aux mots de passe. Décrire une rotation si un vrai secret avait été exposé, sans prétendre qu’elle a été effectuée.

## Défi autonome

Écrire une règle de recherche produisant volontairement un faux positif et expliquer le besoin de revue humaine.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Retirer un secret du dernier fichier ne l’efface pas nécessairement de l’historique d’un dépôt.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab39`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Retirer un secret du dernier fichier ne l’efface pas nécessairement de l’historique d’un dépôt.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — gestion des secrets](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
