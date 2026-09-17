---
tags: [cours, incidents, sources]
maj: 2026-09-13
---
# Cas réels documentés et leçons de méthode

Les faits ci-dessous proviennent des sources indiquées. Les questions et conclusions pédagogiques sont nos analyses, pas des citations des organisations.

## Equifax — 2017

Le Government Accountability Office, organisme d'audit du Congrès américain, documente une fuite de renseignements personnels concernant près de 150 millions de personnes. Son rapport étudie les causes et les réponses organisationnelles. [Rapport officiel du 2018-08-30](https://www.gao.gov/products/gao-18-559).

Application pédagogique : un outil de détection ne suffit pas. Il faut pouvoir identifier le propriétaire d'un actif, vérifier son exposition, appliquer une correction et confirmer son efficacité. Dans Atelier Boréal, on attribuera donc chaque faiblesse à une personne responsable et à une preuve de nouvelle vérification.

Question : si un logiciel figure dans une base de vulnérabilités, quelles informations manquent avant de conclure que notre serveur est exploitable ?

## Uber — septembre 2022

Dans sa mise à jour du 19 septembre, Uber indique qu'un compte de prestataire a été compromis, puis qu'une demande d'approbation de connexion a fini par être acceptée après plusieurs tentatives. L'entreprise rapporte ensuite l'accès à plusieurs systèmes internes. Cette description est celle de l'entreprise à cette date. [Communication officielle](https://www.uber.com/us/en/newsroom/security-update/).

Application pédagogique : l'authentification multifacteur doit être comprise avec ses usages humains. Le cours fait analyser des demandes suspectes sur papier et pratiquer le signalement. Aucune campagne n'est envoyée à des personnes réelles.

Question : une baisse du taux de clic est-elle suffisante si le personnel hésite à signaler une erreur ?

## GitHub — avril 2022

GitHub a annoncé une campagne utilisant des jetons d'autorisation dérobés, émis pour deux intégrations tierces. Le cas concerne la délégation d'accès et les dépendances entre services. [Alerte officielle](https://github.blog/news-insights/company-news/security-alert-stolen-oauth-user-tokens/).

Application pédagogique : une application peut recevoir une permission sans connaître le mot de passe humain. Réinitialiser ce mot de passe n'est donc pas toujours suffisant pour retirer toutes les autorisations déléguées. On examine les permissions, la durée de vie, la révocation et les journaux.

Question : une intégration qui lit les rapports doit-elle pouvoir modifier les dépôts ou inviter de nouveaux utilisateurs ?

## Mirai — appareils connectés

Le ministère américain de la Justice décrit Mirai comme un réseau d'appareils compromis comprenant notamment des caméras, des routeurs et des enregistreurs. Ces appareils ont été utilisés dans des attaques par déni de service distribué. [Communiqué officiel du 2017-12-13](https://www.justice.gov/archives/opa/pr/justice-department-announces-charges-and-guilty-pleas-three-computer-crime-cases-involving).

Application pédagogique : un petit équipement a un système, une identité, des services et un cycle de mise à jour. Son faible prix ne diminue pas les conséquences de son exposition.

Question : pourquoi un réseau de caméras devrait-il être séparé du réseau de facturation ?

## Comment réutiliser un cas sans inventer

Dans un devoir, écrire trois paragraphes distincts : « fait documenté », « mécanisme que ce fait illustre », puis « proposition pour notre laboratoire ». Ne pas attribuer une cause technique précise à un incident si la source ne l'établit pas. Noter la date de la publication : un premier communiqué n'est pas nécessairement le bilan final.

Retour : [Lire le cours](../00-Lire-le-cours.md).
