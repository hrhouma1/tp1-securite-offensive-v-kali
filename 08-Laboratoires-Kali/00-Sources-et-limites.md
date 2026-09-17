---
tags: [cours, kali, sources]
maj: 2026-09-17
statut: proposition-pedagogique
---

# Sources techniques et limites

## Références primaires

Références consultées le 2026-09-17. Les scénarios, fichiers et défis sont pédagogiques. Vérifier aussi l’aide de la version installée.

- [John the Ripper — Kali](https://www.kali.org/tools/john/).
- [CeWL — Kali](https://www.kali.org/tools/cewl/).
- [Crunch — Kali](https://www.kali.org/tools/crunch/).
- [Hashcat — documentation des options](https://hashcat.net/wiki/doku.php?id=hashcat).
- [OpenSSL — génération d’empreintes](https://docs.openssl.org/master/man1/openssl-passwd/).
- [GnuPG — commandes](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Commands.html).
- [Python — fonctions d’empreinte et de dérivation](https://docs.python.org/3/library/hashlib.html).
- [OWASP — authentification](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).
- [RFC 1035 — système de noms de domaine](https://www.rfc-editor.org/rfc/rfc1035.html).
- [Nmap — techniques de scan](https://nmap.org/book/man-port-scanning-techniques.html).
- [Wireshark — manuel de TShark](https://www.wireshark.org/docs/man-pages/tshark.html).
- [OWASP — guide de test web](https://owasp.org/www-project-web-security-testing-guide/).
- [curl — manuel](https://curl.se/docs/manpage.html).
- [Hydra — Kali](https://www.kali.org/tools/hydra/).
- [OWASP — prévention des injections SQL](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
- [OWASP — encodage et prévention XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).
- [OWASP — contrôle d’accès aux objets](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html).
- [OWASP — traversée de répertoires](https://community.owasp.org/attacks/Path_Traversal).
- [Burp Proxy — PortSwigger](https://portswigger.net/burp/documentation/desktop/tools/proxy).
- [Python — sécurité des sous-processus](https://docs.python.org/3/library/subprocess.html#security-considerations).
- [OWASP — gestion des sessions](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).
- [GNU Coreutils — permissions](https://www.gnu.org/software/coreutils/manual/html_node/File-permissions.html).
- [Linux — manuel des listes de contrôle d’accès](https://man7.org/linux/man-pages/man5/acl.5.html).
- [OWASP — gestion des secrets](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html).
- [AWS — politiques et permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).
- [Docker — pratiques de construction](https://docs.docker.com/build/building/best-practices/).
- [Android — manifeste de l’application](https://developer.android.com/guide/topics/manifest/application-element).
- [Eclipse Mosquitto — configuration](https://mosquitto.org/man/mosquitto-conf-5.html).
- [OpenSSL — serveur TLS de test](https://docs.openssl.org/master/man1/openssl-s_server/).
- [Python — tests unitaires](https://docs.python.org/3/library/unittest.html).
- [Rapid7 — module http_version](https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/http/http_version.rb).
- [NIST — sécurité des réseaux sans fil, publication de 2012](https://csrc.nist.gov/pubs/sp/800/153/final).

OWASP (Open Worldwide Application Security Project, projet communautaire de sécurité des applications) fournit plusieurs guides de prévention. NIST (National Institute of Standards and Technology, institut américain de normalisation et de technologie) fournit la référence historique de 2012 sur les réseaux sans fil ; elle n’est pas présentée comme une liste exhaustive des protocoles actuels.

## Manipulations et simulations

Les empreintes, fichiers, requêtes locales, tests du portail et captures de son propre trafic peuvent être manipulés sur Kali. Toutes les données fournies sont inventées.

Les activités suivantes ont une couverture volontairement limitée :

- Windows : représentation simplifiée des droits, sans test réel d’Active Directory, de Kerberos ou de Mimikatz.
- Mouvements latéraux : graphe de communications, sans compromission de plusieurs machines.
- Exfiltration : traces synthétiques, sans transfert vers un tiers.
- Cloud : politiques et réglages fictifs, sans validation des droits effectifs d’un compte.
- Mobile : manifeste lisible, sans application installée ni analyse dynamique.
- Objets connectés : messages locaux, sans appareil physique.
- Wi-Fi : configuration fictive, sans capture radio ni test d’un réseau voisin.
- Sessions web : identité Alice simulée et cookie fixe ; aucun modèle de production.

La contrainte d’une seule Kali est respectée. Elle ne permet pas d’affirmer que toutes les plateformes ont été réellement testées. Distinguer systématiquement « proposé », « exécuté » et « vérifié ».

## Diffusion

Les traces et secrets produits restent dans le dossier de travail ignoré par Git. Le dossier enseignant n’est pas un contrôle d’accès ; choisir les fichiers à distribuer. Le préparateur contient volontairement les réponses de cette banque formative.

Les [cas réels documentés du cours](../04-Ressources/06-Cas-reels-documentes.md) restent distincts du scénario fictif Atelier Boréal.

Retour : [Catalogue](00-Index.md).
