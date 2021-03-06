=================================
Tests de vraisemblance
=================================

Vous pouvez utiliser des tests pour regarder
si une distribution ressemble à ce qu'on aurait
pu obtenir avec une loi.

L'idée est d'observer la différence entre la théorie et nos valeurs.

On va donc comparer un vecteur d'observations (obs) avec un vecteurs des valeurs
théoriques (théorie) (que vous allez obtenir en utilisant la fonction R de la loi
avec des paramètres que vous supposez être bons).

Test d’adéquation/de conformité du Khi deux
---------------------------------------------

| **Fonction** : :code:`chisq.test(obs , p = théorie)`

On a généralement deux lois X (1,...,p) et Y (1, ..., q) alors on a une loi du Khi Deux
qui suit (p-1)(q-1) degrés de liberté (ou alors k-r-1 avec k groupes/classes, r paramètres estimés).

On note df le degré de liberté qu'il faut vérifier. Si R a échoué
a trouvé le bon degré, on devra faire le calcul manuellement.

.. code:: r

	# si R s'est trompé (df invalide), exemple de calcul manuel
	> temp <- sum((obs-théorie)^2/théorie)
	# vous devez donner le vrai df que vous aviez calculé
	> res <- 1-pchisq(temp, df=le_vrai_df)

Test de Anderson-Darling
-----------------------------

| **Fonction**  : :code:`ad.test(obs, loi)` (package ADGofTest)
| **Fonction**  : :code:`ad.test(obs, loi, paramètres_loi...)` (package ADGofTest)

Une loi est par exemple :code:`pnorm`, :code:`ppois` et un paramètre
est par exemple lambda pour une loi de poisson (:code:`ad.test(obs, ppois, lambda)`).

Test de comparaison/sur les proportions
-----------------------------------------

| **Objectif** : trouver la proportion d'individus suivant un certain critère
| **Utilité** : vérifier si loi binomiale, % d'erreurs, ...

	Cas 1 échantillon : on a reçu x succès sur n, p=proba et on veut vérifier si c'est vrai.
		| **Fonction** : :code:`prop.test(x,n,p=proba,correct=FALSE)`
		| **Fonction** : :code:`binom.test(x,n, p=proba)`

	Cas 2 échantillons : on a x succès sur N1 et y sur N2
		| **Fonction** : :code:`prop.test(x=c(x,y), n=c(N1,N2),correct=FALSE)`
		| **Fonction** : :code:`prop.test(as.table(cbind(c(N1,x), c(N2,y))),correct=FALSE)`
		| **Fonction** (package exactmeta) : :code:`study.exact(x,y,N1,N2, BB.grdnum=10000)`

Goodness-of-Fit Test
------------------------------

Minimisation du khi-deux
	| **Fonction** (package vcd) : :code:`goodfit(ech, type = "...", method = "MinChisq")`
	| Le type est : poisson et/ou binomial et/ou nbinomial (vecteur/string)
	| **Utilité** : vérifier si loi poisson ou binomiale ou binomiale négative

	On fait un :code:`summary(goodfit)` pour voir le résultat.

Méthode du maximum de vraisemblance
	| **Fonction** (package vcd) : :code:`goodfit(ech, type = "...", method = "ML")`
	| **Note** : tout pareil que pour la minimisation du khi-deux

Test de distribution
------------------------

ANOVA unidirectionnelle sur les rangs (Test de Kruskal et Wallis)
	| **Fonction** : :code:`kruskal.test(quant ~ qual, data = ech)`
	| **Robustesse** : échantillons d'au moins 15 individus

	Il s'agit de tester si des échantillons sont issus d'une même distribution.

Test de la somme des rangs
---------------------------

Test de Mann–Whitney U
	| **Fonction** : :code:`wilcox.test(ech~quant, data=ech, paired=FALSE, exact=FALSE)`
	| **Utilité** : marche si moins de 30 individus, et si les populations ne sont pas de la même taille

	Aussi appelé Mann–Whitney–Wilcoxon (MWW) ou Wilcoxon–Mann–Whitney test.