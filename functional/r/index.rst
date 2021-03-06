.. _r:

================================
Langage R
================================

| :math:`\color{grey}{Version \ 0.3.25}`
| :math:`\color{grey}{Dernière \ édition \ le \ 09/02/2021}`

1. Introduction
===================

Le R est un langage complet permettant de faire des statistiques. Les fonctions
(ouvrir un fichier, ...) marchent sous tout système d'exploitation.

Comme en OCaml/Python/..., vous pouvez écrire un fichier :code:`.R`
ou alors écrire directement dans l'interpréteur.

Vous pouvez coder du R dans RStudio ou dans IntelliJ.

Quelques points

	* en mode interpréteur, taper le nom d'une variable affiche sa valeur
	* la documentation est généralement écrite en RMarkdown

Vous allez utiliser des packages (librairies) contenant des fonctions/constantes/... Vous
pouvez voir la liste des packages installés avec :code:`installed.packages()`,
installer un package avec :code:`install.packages("nom")`.
Enfin pour l'utiliser dans le code, il faudra le charger (sauf s'il l'est déjà
par défaut), ceci est fait avec :code:`library("nom");`.

2. Notes d'introduction
===================================

Vous pouvez obtenir de l'aide sur une fonction avec :code:`?nom_fonction`
qui sous RStudio/IntelliJ ouvre une page de documentation. Vous
pouvez faire :code:`args(fonction)` pour voir ses arguments. Vous
pouvez voir des exemples d'utilisation avec :code:`example(fonction)`.
Enfin, on peut utiliser :code:`body(fonction)` pour voir le corps
d'une fonction.

Les commentaires se font avec :code:`#`. Pas de symbol en fin de ligne.
Vous pouvez mettre plusieurs instructions sur une ligne avec des :code:`;` entre.

La commande :code:`ls` liste toutes les variables. Pour nettoyer
toutes vos variables, tapez :code:`rm(list=ls())`.

Vous pouvez obtenir de l'aide avec :code:`help.start()`.

La fonction :code:`print()` permet d'afficher
quelque chose en mode compilé.

La fonction :code:`data()` permet d'afficher la liste
de tous les jeux de données disponibles ou d'en charger un.

3. Particularités du R
========================

Le R est faiblement typé, vous pouvez trouver le type d'une variable avec :code:`class(var)`
ou déclarer une variable avec :code:`var <- valeur` (par exemple :code:`cinq <- 5` ou
:code:`cinq <- as.numeric(5)`).

La plupart des opérations et conditions (+,-,<=,>, ...) ainsi que les structures
basiques (if, ...). Notez cependant que R fait une addition qu'il juge appropriée selon
les types ou si des tableau/... sont de taille différente alors il les recycle.

Vous n'allez probablement jamais faire de branchements car vous pouvez directement
utiliser les indices comme :code:`tab[tab > 10] <- 0` qui mets 0 à tous les valeurs
du tableau étant plus grandes que 10. Alternativement, les fonctions apply permettent
d'appliquer une fonction sur tous les éléments donc sont très utilisées.

Enfin, vous comprendrez mieux les notions suivantes si vous lisez le petit résumé
de Statistiques et R.

.. toctree::
	 :maxdepth: 1

		Types en R                  <files/part/types>
		Opérations et Conditions    <files/part/op>
		Structures et apply         <files/part/struct>
		Statistiques et R           <files/part/stats>
		Note sur les blocs          <files/part/blocs>

Petite note sur les noms. Généralement vous trouver des noms de la forme :code:`nom.nom`,
généralement cela est uniquement sémantique (sinon je crois c'est lié à la généricité)
mais c'est pour regrouper les variables (au sens non littéral) dans un groupe sémantique.
Par exemple :code:`ozone` qui dérive en :code:`ozone.summer` et :code:`ozone.winter`
pour les observations de l'ozone en été et en hiver (cela peut être sur des variables, fonctions, ...).

Enfin, vous n'êtes pas toujours obligé d'écrire les noms complets des arguments passés à
une fonction ou certains trucs évidents par exemple TRUE s'écrit aussi T ou dans
une fonction :code:`hist(..., probability = valeur)` on peut écrire
:code:`hist(..., prob = valeur)` par exemple donc un diminutif.

4. Types complexes
========================

.. toctree::
	 :maxdepth: 1

		Vecteurs    <files/types/c>
		Matrices    <files/types/matrix>
		Tables      <files/types/table>
		Listes      <files/types/list>
		Facteurs    <files/types/factor>
		data.frame  <files/types/df>

Voici quelques fonctions utiles sur les vecteurs (voir sur les listes,
matrices, tables, ...).

	* :code:`head(v)` pour voir les premières valeurs d'un vecteur
	* :code:`tail(v)` pour voir les dernières valeurs d'un vecteur
	* :code:`length(vecteur)` : retourne la taille
	* :code:`dim(vecteur)` : retourne la taille (plus utilise pour les matrices)
	* :code:`which.min(v) ou which.max(v)` : retourne l'indice du min/max
	* :code:`which(v opérateur valeur)` : retourne les indices des éléments selon la condition
	* :code:`rev(v)` : inverse
	* :code:`sum(v)` : somme de tous les éléments
	* :code:`prod(v)` : produit de tous les éléments
	* :code:`attributes(vecteur)` : voir les attributs (dim, ...)
	* :code:`any(v opérateur valeur)` : retourne true un des éléments respectent la condition
	* :code:`all(v opérateur valeur)` : retourne true tous les éléments respectent la condition
	* :code:`sort(v)` : trie les données
	* :code:`View(v)` : voir le contenu d'un vecteur
	* :code:`identical(v1,v2)` : savoir si deux vecteurs sont indentiques
	* :code:`valeur %in% v` : savoir si valeur est dans v

5. Fonctions
========================

Je suppose que vous avez remarqué qu'on appelle une fonction :code:`nom(arguments, ...)`
mais vous pouvez aussi faire :code:`nom(nom_argument = valeur, ...)`. En fait dans la deuxième
version, vous n'êtes pas obligé de donner des valeurs dans l'ordre donc c'est assez pratique.

Généralement il y a beaucoup d'argument ayant une valeur par défaut donc facultatif, vous n'avez donc
pas besoin de leur donner une valeur, vous pouvez voir la doc avec :code:`?nom_fonction` (plus d'infos en intro).

On utilise :code:`function (arguments)` ou fonction :code:`fonction (nom = v_default, ....)`
pour déclarer une fonction.

.. code:: R

		> modulo <- function (x, mod=2){
		 if(mod < 2) {
		  warning(paste(x," doit être >= à 2"));
		  mod <- 2
		 }
		 # on pourrait ne pas mettre return car
		 # x %% mod retourne déjà le résultat
		 return(x %% mod)
		}
		> modulo(5)
		[1] 1
		> modulo(5,3)
		[1] 2
		> modulo(5, -1)
		Warning in modulo(5, -1) : 5  doit être >= à 2
		[1] 1
		> modulo(mod = 3, 5)
		[1] 2

On se rappelle le point sur les blocs, si une fonction ne retourne rien, elle retourne la valeur
de sa dernière expression (si celle ci retourne quelque chose ce qui n'est pas cas d'une assignation par exemple).
Les variables, contrairement aux blocs normaux n'existent que dans le bloc mais si R
ne trouve pas une variable, il va voir dans le bloc d'au dessus.

6. Fonctions utilitaires
===========================

...

7. Maths en R
========================

Bric à brac
	* :code:`pi` : variable qui contient pi
	* :code:`runif(n)` : génère n nombres aléatoires entre 0 et 1
	* :code:`choose(n,k)` : choisi n éléments parmi k (vecteur)
	* :code:`factorial(n)` : n factoriel
	* :code:`min(v)` : valeur min
	* :code:`max(v)` : valeur max
	* :code:`seq(from = x, to = y, length = l)` : suite de l valeurs séquentielles de [x,y]
	* :code:`rep(v, n)` : répète n fois v
	* :code:`sample(v, n)` : extrait un échantillon (i.i.d)

Fonctions de stats basiques

	* :code:`summary(x)` : calcule la moyenne, ...
	* :code:`mean(x)` : moyenne
	* :code:`median(x)` : médiane
	* :code:`var(x)` : variance
	* :code:`cov(x)` : covariance
	* :code:`cor(x)` : corrélation

8. Fonctions graphiques
=============================

...

9. RMarkdown
===========================

Le RMarkdown (fichier .Rmd) est basé sur le Markdown donc vous aurez
plus d'infos sur le cours de Markdown. Voici un exemple
de fichier, avec des métadonnées.

.. toctree::
    :maxdepth: 1

		Synthèse Rmd                   <files/rmd/t>
		Détails sur les blocs de code  <files/rmd/bloc>

9. Exercices
==============

.. toctree::
    :name: exercices
    :maxdepth: 1

		Introduction				<exercices/intro>

-----

**Crédits**
	* Jean R. LOBRY (Université de Lyon)
	* Brigitte SCHAEFFER (INRA-Jouy)
	* Sophie SCHBATH (INRA-Jouy)
	* Quentin RAMSAMY--AGEORGES (étudiant à l'ENSIIE)

**Références**
	* "Take only pictures, leave only footprints."
	* Swirl, R programming
	* https://pbil.univ-lyon1.fr/R/pdf/lang01.pdf
	* https://pbil.univ-lyon1.fr/R/pdf/lang02.pdf
	* https://pbil.univ-lyon1.fr/R/pdf/lang03.pdf
	* https://pbil.univ-lyon1.fr/R/pdf/lang04.pdf
	* https://fxjollois.github.io/cours-2016-2017/initiation-a-r-tp1.html
	* https://fxjollois.github.io/cours-2016-2017/index.html
	* https://fr.wikibooks.org/wiki/Programmer_en_R/Les_fonctions_statistiques_de_base
	* https://www.dunod.com/sites/default/files/atoms/files/9782100712861/Feuilletage.pdf
	* https://rmarkdown.rstudio.com/lesson-1.html
	* https://abcdr.thinkr.fr/redaction-markdown/
	* https://rstudio.com/wp-content/uploads/2015/03/rmarkdown-reference.pdf
	* http://www3.jouy.inra.fr/miaj/public/formation/initiationRv10.pdf
	* https://stackoverflow.com/questions/7526467/what-does-the-dot-mean-in-r-personal-preference-naming-convention-or-more
	* https://stats.stackexchange.com/questions/10712/what-is-the-meaning-of-the-dot-in-r
	* https://www.reddit.com/r/datasets/comments/exnzrd/coronavirus_datasets/
	* https://rviews.rstudio.com/2020/03/05/covid-19-epidemiology-with-r/
	* https://www.dunod.com/sites/default/files/atoms/files/9782100712861/Feuilletage.pdf