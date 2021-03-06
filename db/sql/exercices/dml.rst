================================
Insert, Update, Delete
================================

Niveau débutant
***********************

1/1 Que le spectacle continue
-------------------------------------------------

.. note::

	| Fichier de la base à importer (mariadb) : :download:`setup.sql <../../../assets/db/bases/spectacles_ensiie_1a_import.sql>`
	| Fichier de la base à importer (postgre) : :download:`setup.sql <../../../assets/db/bases/spectacles_ensiie_1a_import_p.sql>`

1. Donnez les expressions SQL permettant d’ajouter les personnes suivantes :

.. code:: none

		Personne(’A01’, ’Boss of the’, ’Base’)
		Personne(’S01’, ’Boss of the’, ’Show’)
		Personne(’G01’, ’Boss of the’, ’Guichetier’) -- à référencer comme Guichetier
		Personne(’G02’, ’Another one’, ’Guichetier’) -- à référencer comme Guichetier

2. Donnez les expressions SQL permettant de répondre aux questions suivantes :

	(a)
		Quels sont les noms et prénoms des guichetiers.
	(b)
		Pour chaque type de spectacle, combien de spectacles ont eté proposés en 2013 ?
	(c)
		Quel est le prix moyen d’une place de type 'theatre' pour l’année 2013 ?
	(d)
		Quel est le chiffre d’affaire des spectacles de type 'theatre' pour l’année 2013 ?
	(e)

			Quelle requête permettrait d’obtenir l’attribut dérivé n_spectacle de la relation Billet ?
			Sans définir explicitement un déclencheur, on se placera dans le cadre où l’on a accès aux attributs
			NEW.n_billet, NEW.n_salle, NEW.b_date, NEW.nom_client d’un billet qu’on est en train d’insérer

.. note::

	**Aide (e)** : Un déclencheur ou trigger est défini dans le cours de PL/SQL. En gros, lorsque vous allez
	faire un insert, vous n'allez pas donner l'attribut dérivé. Le trigger va être déclenché et va avoir pour
	travail de remplir cette attribut (n_spectacle) avec une valeur.

	Vous devez écrire la requête SQL qui donne la valeur a donner à n_spectacle. Les valeurs du tuple qui va être inséré sont
	contenues dans NEW, donc vous pouvez utiliser NEW.attribut dans un where par exemple.
	- Calistro <wtf la question>

.. toctree::
   :maxdepth: 1

	Proposition de correction n°1			<dml/d1>

| :code:`[TAG] ENSIIE IBD TDM1 2018 S1`
| :code:`[TAG] ENSIIE IBD TDM1 2019 S1`
| :code:`[TAG] ENSIIE IBD TDM1 2020 S1`

Niveau supérieur
***********************

aucun

Niveau avancé
***********************

aucun

|

-----

**Crédits**
	* Marie SZAFRANSKI (enseignant à l'ENSIIE)