---
tags: [cours, laboratoire, kali, securite-offensive]
maj: 2026-09-17
statut: proposition-pedagogique
laboratoire: 13
semaine_associee: 6
duree_minutes_indicative: 40
---

# Laboratoire 13 — Déjouer un courriel d’hameçonnage fictif

## Mission et contexte

Analyser un message fourni comme texte, sans ouvrir son lien et sans envoyer de courriel.

Cas d’usage professionnel reconstitué pour l’entreprise fictive Atelier Boréal. Les comptes, personnes, journaux et secrets fournis sont synthétiques. Les résultats attendus ci-dessous sont des critères d’exercice, pas des observations sur une organisation réelle.

## Préparation

- Terminer la [préparation commune](../00-Preparation-Kali.md).
- Outils : Python 3, bibliothèque email.
- Mode : Analyse de message synthétique.
- Lire la [théorie associée à la semaine 6](../../02-Semaines/Semaine-06-Ingenierie-sociale/01-Cours/Ingenierie-sociale-et-facteurs-humains.md).
- Dans le terminal, rester dans le dossier `08-Laboratoires-Kali`, pas dans le sous-dossier de cette fiche. Les chemins des commandes partent tous de ce dossier.
- Si la fiche exige le service local : laisser `python3 outils/serveur.py` ouvert dans un autre terminal.

## Durée et objectif de réussite

Durée indicative : 40 minutes, hors installation des logiciels. La réussite exige une manipulation ou une analyse reproductible, une explication et une correction vérifiée ou explicitement proposée. Aucun point n’est lié à la vitesse d’une attaque.

## Comprendre avant de manipuler

L’hameçonnage cherche à provoquer une action par tromperie. Un nom d’expéditeur rassurant n’authentifie pas le domaine ni la demande. Une analyse doit distinguer indice suspect et preuve : l’urgence seule ne prouve pas une fraude.

<details>
<summary>Comprendre simplement</summary>
<p>Un uniforme dessiné sur une enveloppe ne garantit pas l’identité de la personne qui l’a envoyée.</p>
</details>

## Périmètre et point d’arrêt

Utiliser uniquement les fichiers créés pour ces ateliers et les services explicitement démarrés sur `127.0.0.1`. Ne pas tester de compte réel, de site public, de réseau voisin ou d’appareil tiers. Les adresses et noms présents dans des scénarios restent des données à lire, pas des cibles à contacter. Arrêter avec `Ctrl+C` en cas de cible inattendue, de charge anormale ou de donnée non fictive.

## Manipulation guidée

### 1. Prédire

Écrire le résultat attendu et ce qui pourrait l’infirmer. Relever les outils disponibles et les fichiers d’entrée. Pour une expérience avant/après, conserver les deux états avec des noms distincts.

### 2. Réaliser

```bash
python3 - <<'PY'
from email import policy
from email.parser import BytesParser
from pathlib import Path
message = BytesParser(policy=policy.default).parsebytes(Path("travail/courriel.eml").read_bytes())
for champ in ["From", "To", "Subject", "Date"]:
    print(champ, ":", message[champ])
print(message.get_content())
PY
```

Le parseur lit les en-têtes et le corps sans rendre une page web ni contacter le domaine.

### 3. Interpréter

Trois indices sont décrits, avec une action de vérification indépendante pour chacun.

Comparer cette attente aux sorties réellement obtenues. Un résultat différent doit être décrit avec sa cause probable et un test de vérification, jamais remplacé par une capture empruntée.

## Corriger et effectuer un contre-test

Rédiger un message de sensibilisation qui conseille de retrouver soi-même le canal officiel plutôt que de répondre à l’expéditeur suspect.

## Défi autonome

Créer une version légitime fictive ne demandant aucun secret et comparer le parcours utilisateur.

<details>
<summary>Indice — à ouvrir après un premier essai</summary>
<p>Comparer boreal.example et boreal-support.example ; décrire la différence exacte sans supposer un historique inexistant.</p>
</details>

## Preuves à remettre

1. Une courte description du périmètre et du résultat prédit.
2. Les commandes ou étapes réellement exécutées, avec une sortie lisible et le nom du fichier d’entrée.
3. Une explication du résultat avec au moins une limite.
4. Une correction et son contre-test ; pour une simulation documentaire, identifier clairement ce qui n’a pas été déployé.

Conserver les pièces dans `travail/preuves/` avec le préfixe `lab13`. Ne pas joindre tout le dictionnaire rockyou.txt, une clé privée ou un mot de passe réel. Le [barème commun proposé](../00-Evaluation-et-progression.md) évalue la méthode, la preuve et le raisonnement.

## Dépannage

Commencer par vérifier le dossier courant et les prérequis. Une commande absente se traite avec la préparation commune ; une connexion refusée se traite en vérifiant le serveur local. Ne pas augmenter le périmètre pour contourner un échec.

Comparer boreal.example et boreal-support.example ; décrire la différence exacte sans supposer un historique inexistant.

## Nettoyage et restauration

Arrêter avec `Ctrl+C` uniquement les services et captures démarrés pour cette expérience. Conserver ses preuves. Ne pas toucher aux originaux du cours ni aux fichiers système. Pour recommencer complètement, suivre la procédure de conservation et de préparation d’un nouveau dossier de travail dans la [préparation commune](../00-Preparation-Kali.md).

## Sources et liens

- [OWASP — authentification](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).
- [Sources techniques et limites de la banque](../00-Sources-et-limites.md).
- [Cas réels documentés du cours — distincts de notre scénario fictif](../../04-Ressources/06-Cas-reels-documentes.md).
- [Retour au catalogue des 50 laboratoires](../00-Index.md).
