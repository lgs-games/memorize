.. _cypher:

================================
Bases de données Graphes
================================

| :math:`\color{grey}{Version \ 1.0.1}`
| :math:`\color{grey}{Dernière \ édition \ le \ 17/12/2020}`

1. Introduction
===================================

Une nouveau type de base de données autre que relationnelles apparu vers 2010
sont les bases de données "graphes".

Elles ont étés introduites par/pour les entreprises
comme Google, Facebook, Twitter, ... pour pouvoir gérer plus facilement des données
complexes et différentes (hétérogènes).

On parle de :code:`NOSQL` (NotOnlySQL) pour pas seulement SQL car il s'agit d'un ajout ou d'une surcouche
qui complète les SGBD relationnels.

.. toctree::
	 :maxdepth: 1

		Les points clefs         <intro/key>
		L'idée                   <intro/idea>

Motifs graphe
	Il s'agit d'une règle, par exemple x-motif->y. On liste toutes les arêtes avec leurs valuations en on obtient
	un ensemble avec toutes les valeurs x et leur y associé qui correspondent a la règle. Apparemment c'est utile pour
	faire des recherches.

2. Présentation de Cypher
==================================

Cypher est le langage utilisé dans Neo4J, une SGBD graphe.

.. toctree::
	 :maxdepth: 1

		 Représentation d'un nœud        <rep/node>
		 Représentation d'une arête      <rep/vertex>
		 Requêtes Cypher : base          <rep/cypher>
		 Requêtes Cypher : DDL           <rep/cypher2>

Requêtes avancées

.. toctree::
	 :maxdepth: 1

		 Listes                         <adv/list>
		 Fonctions                      <adv/functions>
		 Clauses avancées               <adv/clauses>

3. Exercices
==================================

.. toctree::
	 :maxdepth: 1

		 Cypher                 <exercices/cypher>
		 Non triés              <exercices/non_rank>

-----

**Crédits**
	* Stefania DUMBRAVA (enseignante à l'ENSIIE)
	* Cypher Neo4J Doc (https://neo4j.com/developer/cypher/)
	* Quentin RAMSAMY--AGEORGES (étudiant à l'ENSIIE)

**Références**
	* https://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_orient%C3%A9e_graphe
	* https://neo4j.com/docs/cypher-manual/current/