.. _git:

================================
Git
================================

| :math:`\color{grey}{Version \ 1.0.0}`
| :math:`\color{grey}{Dernière \ édition \ le \ 11/01/2021}`

Git est un gestionnaire de version de votre code. Il vous permet de créer des sauvegardes
(appelées **commits**). Il facilite également le travail de groupe, en permettant a chacun
de partir d'un commit, de travailler de son côté (sur une **branche**) puis de fusionner
le code afin d'intégrer les modifications de chacun (**merge**).

1. Introduction
===================================

Vous pouvez utiliser un serveur git comme `Github <https://github.com/>`_ ou `GitLab <https://about.gitlab.com/>`_
ou héberger un serveur git chez vous avec `Gogs <https://gogs.io/>`_ par exemple.

Toutes les commandes :code:`git` sont dans le package git et sont appelées
en mettant :code:`git <commande> <autres arguments>`.

Lors de votre toute première utilisation, vous devez spécifier votre nom+email.
Cela se fait avec les commandes

.. code:: bash

	git config --global user.name "Votre nom"
	git config --global user.email "Votre email"

Pour éviter de devoir vous connecter a chaque commit (super relou), vous pouvez configurer une clef
ssh (tuto : https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

De façon générale, il faut générer un fichier .ssh/id_rsa.pub, et le copier
dans la partie ssh des paramètres de votre compte git.

Si vous voulez avoir des commits vérifiés (donc marqué vérifié a côté de vos commits, rien de plus
donc totalement optionnel),
alors vous avez un tuto ici : https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-gpg-key.

2. Les commandes basiques
======================================

:code:`git add <fichiers>` (ou git add . pour tout ajouter)
	Seulement les fichiers ajoutés seront commits.

:code:`git commit -m "nom_du_commit"`
	Création de la sauvegarde, ayant pour nom \"nom_du_commit\". Elle est locale, il faudra l'envoyer
	sur le serveur.

:code:`git push`
	Envoi tous les commits locaux sur le serveur.

:code:`git pull`
	Récupère la dernière version du dépôt.

:code:`git clone ...`
	Télécharge le répertoire ... (donner une url en http ou ssh) dans votre dossier courant.

:code:`git status`
	Indique le status du dépôt, très utile. Donne le nombre de commits non envoyés, les fichiers ajoutés
	non commités et les fichiers non ajoutés.

3. Les commandes avancées
=============================

:code:`git branch <nom>`
	Créer une branche (=copie de votre code et de tous les commits précédents)
	depuis votre branche actuel (master par défaut).

:code:`git checkout <nom>`
	Vous déplacer sur une autre branche (attention, les modifications locales sont perdues)

:code:`git merge <nom>`
	Fusionne votre branche actuelle et une branche <nom>. Si des fichiers ont étés modifiés dans les deux branches,
	alors vous devrez manuellement choisir quoi garder (vous allez voir des fichiers bizarres ============>...
	et faudra supprimer le code non voulu : c'est relou).

	Pour faire des merge un peu plus facile, vous pouvez utiliser un IDE comme Intellij qui vous montre une interface
	avec 3 fichiers : celui de votre branche, le résultat et celui de l'autre branche. Les lignes modifiés sont en couleur.
	Vous pouvez choisir quoi garder en cliquant sur les flèches et c'est super pratique.

4. Bonne conduite
=================================

...

5. Github/Fonctionnalités expert
========================================

...

-----

**Crédits**
	* Quentin RAMSAMY--AGEORGES (étudiant à l'ENSIIE)

**Références**
	* aucune