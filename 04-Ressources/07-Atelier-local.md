---
tags: [cours, laboratoire, environnement]
maj: 2026-09-13
---
# Atelier Boréal — environnement local des exemples

L'atelier comprend un catalogue de trois produits et deux factures fictives. Il permet de comparer une recherche vulnérable et une recherche paramétrée, un contrôle de propriété absent et présent, ainsi qu'un affichage de texte interprété ou échappé.

Le programme est fourni dans [atelier_boreal.py](Atelier-Boreal/atelier_boreal.py). Il utilise Python 3 et sa bibliothèque standard. Il fonctionne dans Kali Linux ou sur un poste disposant de Python avec son module de base relationnelle. Le plan privilégie VMware et Kali ; cet atelier est un complément local, pas un remplacement du laboratoire existant.

## Démarrer

Dans un terminal ouvert dans le dossier `04-Ressources/Atelier-Boreal` :

```bash
python3 atelier_boreal.py
```

Sur Windows, utiliser `py atelier_boreal.py` ou `python atelier_boreal.py` selon l'installation. Ouvrir ensuite [l'atelier local](http://127.0.0.1:8000).

Le programme écoute uniquement sur la boucle locale. Il ne reçoit aucun nom de cible externe et ne lance aucune commande système. Les données sont recréées en mémoire ; l'application ne lit pas les fichiers privés du poste. Fermer avec Ctrl+C.

## Les observations prévues

| Adresse après le nom du serveur | Résultat attendu |
|---|---|
| `/health` | État prêt, identité simulée Alice |
| `/catalogue?nom=Casque` | Un produit |
| `/catalogue-corrige?nom=Casque` | Le même produit |
| `/facture?id=202` | Facture de Benoît visible par Alice |
| `/facture-corrige?id=202` | Refus |
| `/facture-corrige?id=101` | Facture d'Alice accessible |
| `/echo?texte=%3Cb%3EBonjour%3C%2Fb%3E` | Bonjour apparaît en gras |
| `/echo-corrige?texte=%3Cb%3EBonjour%3C%2Fb%3E` | Les balises sont affichées comme texte |

<details>
<summary>Comprendre simplement : une identité fixée pour étudier une seule règle</summary>
<p>L'atelier considère toujours que la personne est Alice. Il ne contient pas un véritable système de connexion. Cela permet d'étudier le contrôle de propriété sans ajouter la complexité des sessions. Dans une vraie application, l'identité doit provenir d'un mécanisme d'authentification fiable.</p>
</details>

## Rechercher une valeur construite

```bash
curl --get --data-urlencode "nom=' OR 1=1 --" http://127.0.0.1:8000/catalogue
curl --get --data-urlencode "nom=' OR 1=1 --" http://127.0.0.1:8000/catalogue-corrige
```

La première commande utilise une entrée qui transforme la logique de la recherche vulnérable ; elle renvoie les trois produits fictifs. La seconde transmet la même valeur au chemin corrigé ; aucun produit n'a ce nom. L'option `--data-urlencode` encode la valeur pour le transport, ce qui n'est pas la même chose que corriger la requête côté serveur.

Pour Windows PowerShell, remplacer `curl` par `curl.exe` si nécessaire. Les résultats dépendent du démarrage du serveur ; une erreur de connexion n'est pas un résultat de sécurité.

## Vérifier les exemples

```bash
python3 verifier_atelier.py
```

Ce programme compare les fonctions directement, sans cible réseau. Les vérifications couvrent la recherche normale, la comparaison vulnérable/corrigée, l'apostrophe, l'accent, les factures, l'affichage et les routes.

## Limites pédagogiques

Le programme illustre quelques défauts, sans être une application professionnelle. La page d'affichage bloque volontairement les scripts par sa politique de contenu. L'expérience avec les balises démontre une injection de balisage, pas une prise de contrôle du navigateur.

Le programme ne remplace pas les activités Windows, les réseaux virtuels ou l'application vulnérable déjà présente dans le premier travail pratique. Ces environnements demandent une validation sur les postes d'enseignement avant utilisation en classe.

Retour : [Lire le cours](../00-Lire-le-cours.md).
