.. _web_g:

================================
Web
================================

| :math:`\color{grey}{Version \ 0.5.8}`
| :math:`\color{grey}{Dernière \ édition \ le \ 25/01/2021}`

1. Introduction
===================

On définit le Web par les pages web que vous consultez
en tapant une URL (ex : https://duckduckgo.com/).

Les pages web sont écries en HTML, le style est définit en CSS. Lorsque vous tapez
une url, alors elle est envoyée à un serveur qui retourne une page HTML qui est affichée dans votre navigateur.
Vous pouvez exécuter du code sur le serveur (ex: mettre la date du jour, utiliser des boucles, ...)
avec PHP. Enfin, vous pouvez
exécuter du code dans la navigateur du client (ex: animations, ...) avec le JavaScript.

Il existe de nombreuses personnes qui n'aiment pas le web, donc il existe de nombreux moyens
de coder des sites sans faire de HTML/CSS/...

Résumé

	* HTML5 : contenu d'une page affichée (fichier .html)
	* CSS : style d'une page (fichier .css)
	* JavaScript : animations dans le navigateur (fichier .js)
	* PHP (+SQL) : code qui modifie l'HTML avant de l'envoyer, côté serveur (fichier .php)

On parle de FrontEnd : HTML/CSS/JS et BackEnd : PHP/SQL.

Il est recommandé de lire les points suivants car c'est utile et certains
vous feront gagner du temps.

.. toctree::
	 :maxdepth: 1

		Note sur les frameworks     <note/framework>
		Note sur les protocoles     <note/proto>
		Note sur la console         <note/cons>
		Note sur FTP                <note/ftp>
		Note sur les caractères     <note/char>

Autres sujets plus généraux (pour les pros)

.. toctree::
	 :maxdepth: 1

		.htaccess         <note/htaccess>
		robots.txt, ...   <note/robots>
		Captcha           <note/captcha>

2. Organisation
==================

Généralement, la structure d'un site web (simple) est de la forme

.. code:: none

	/
	-----
	----- assets/
	---------- css/
	--------------- style.css
	---------- js/
	--------------- [...].js
	---------- img/
	--------------- [...].png
	----- pages/
	---------- [...].html
	----- index.html

Cette disposition permet de voir clairement les éléments du site (donc
pas tout dans le même dossier).

Lorsque vous tapez une url

	* :code:`https://mangadex.org/title/46592/kill-the-hero`
	* :code:`https://mangadex.org/` : correspond à la racine
	* :code:`title/46592/kill-the-hero` : depuis la racine dossier title/.../kill-the-hero/

Lorsqu'il n'y a pas affiché [...].html ou [...].php ou ... donc aucun nom de fichier
alors c'est que le fichier index (html ou php ou ...) est utilisé.

3. HTML
====================

Pour faire tourner de l'HTML, il suffit de déposer un .html dans votre navigateur.

Alternativement si vous êtes sous linux et avez un :code:`public_html`
alors vous pouvez y accéder via une url (généralement
de la forme :code:`https://domaine/~nom_utilisateur/fichier.html` si fichier.html
est dans public_html). Si ce dossier n'est pas configurer, alors regarder
le cours pour "setup" un serveur apache.

Sinon vous pouvez utiliser le moyen vu en PHP (wamp) qui est un logiciel
qui "setup" un serveur apache lorsqu'il est lancé (donc pas permanent).

4. CSS
====================

Un fichier généralement appelé style.css. Voir le cours pour l'appliquer
au HTML. Aucune configuration requise.

5. JS
====================

Un fichier .js. Permet d'exécuter des scripts dans le navigateur. Aucune configuration requise.

Vous noterez que dans la partie console de la console F12 alors vous pouvez directement
taper du javascript sur n'importe quel site.

6. PHP
====================

Vous pouvez faire de l'HTML dans un PHP mais pas l'inverse. Vous devez
avoir une machine qui fait office de serveur (si c'est votre
cas, l'URL sera http://localhost).

Pour ce faire, vous pouvez configurer un serveur apache (voir le tutoriel).

-----

**Crédits**
	* Tous les contributeurs des autres cours de web, indirectement
	* Quentin RAMSAMY--AGEORGES (étudiant à l'ENSIIE)

**Références**
	* https://filezilla-project.org/
	* https://www.w3schools.com/
	* https://validator.w3.org/
	* https://codeigniter.com/
	* http://robots-txt.com/
	* https://www.w3schools.com/howto/default.asp
	* https://httpd.apache.org/docs/current/howto/htaccess.html
	* https://www.godaddy.com/garage/htaccess-tutorial-and-cheat-sheet/
	* https://www.contentkingapp.com/academy/redirects/
	* https://searchfacts.com/robots-txt-allow-disallow-all/
	* https://www.semrush.com/blog/beginners-guide-robots-txt/