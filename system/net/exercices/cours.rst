================================
Comprendre les notions
================================

Niveau débutant
***********************

1. Adresses IPV4, masques et attribution
--------------------------------------------

Pour chacun des adresses, indiquer si c'est une adresse de host ou de réseau.
Lorsque c'est une adresse réseau, on en calculera le netmask, le broadcast mask
et le nombre maximal de machines.

1. :code:`89.218.0.0/14`
2. :code:`192.24.88.0/21`
3. :code:`194.10.0.0/17`
4. :code:`157.31.112.0/19`

.. toctree::
   :maxdepth: 1

	Proposition de correction n°1			<cours/d1>

| :code:`[TAG] IUTSF ASR TD1 2019 S2`

2. Attribution d'adresses
-----------------------------------

Un fournisseur d'accès (ISP) dispose de la plage d'adresses
IP 85.85.160.0 - 85.85.163.255.

(a) \
	Montrer qu'elle correspond bien à un réseau. En donner l'adresse et le masque. Écrire le réseau
	en notation CIDR.

(b) \
	Trois clients C1, C2, C3 demandent un accès internet. Le client C1 pour un réseau de 502
	machines, C2 pour 510 machines et C3 pour 514 machines. L'ISP pourra-t-il satisfaire toutes les demandes ?

	1. Si oui, faire une affectation avec le minimum de perte.
	2. \
		Sinon, indiquer le nombre maximum de clients qu'il peut satisfaire et faire une affectation avec
		le minimum de perte, en précisant quels sont ces clients.

	Donner l'adresse et le masque de chaque sous-réseau attribué ainsi que sa notation CIDR
	et indiquer combien de machines on peut mettre sur chaque sous-réseau attribué.

.. toctree::
   :maxdepth: 1

	Proposition de correction n°1			<cours/d2>

| :code:`[TAG] IUTSF ASR TD1 2019 S2`

3. Découverte
------------------------------

1. Donnez la liste des interfaces réseaux de votre machine (ifconfig/ip)

	* Quel est le type de l'interface eno1 (ou eth0) ? Est-elle active ? Quelle est son adresse MAC ?
	* \
		La première moitié de cette adresse est un OUI (identificateur unique d'organisation).
		En utilisant le fichier suivant (attention très long : http://standards-oui.ieee.org/oui/oui.txt),
		donnez le nom du fabricant de votre carte réseau.
	* Quelle adresse IPv4 lui correspond ? de broadcast ? de sous-réseau ?
	* A quoi correspondent les statistiques RX et TX ?
	* Quel est le type de l'interface lo ? A quoi sert-elle ?

2. Quel est l'adresse IPv4 du réseau auquel appartient votre machine ? Est-ce un WAN ou un LAN ?

3. Expliquez le résultat de la commande :code:`hostname`.

4. La commande ping vous permet (entre autres) de savoir si une machine (configurée pour répondre !) est visible à partir de la votre.

	* expliquez :code:`ping 127.0.0.1`
	* en utilisant le cache arp (:code:`arp`) après un ping, donnez l'adresse ip de duckduckgo.com.

5. Pouvez-vous "pinger" toutes les machines de votre réseau ? Comment ?

6. La commande route permet d'afficher la table de routage de votre machine. Expliquez le résultat.

.. toctree::
   :maxdepth: 1

	Proposition de correction n°1			<cours/d3>

| :code:`[TAG] IUTSF ASR TP1 2019 S2`

4. Synthèse des notions
===================================

1. \
	Donnez le /n du masque réseau, les numéros de réseau et d’hôte et
	l’adresse de broadcast pour IP=225.67.129.30 et MR=255.255.192.0.

2. \
	Donnez le masque réseau, les numéros de réseau et d’hôte et l’adresse
	de broadcast pour IP=225.67.127.30/19.

3. \
	Donnez le masque réseau et son /n puis les numéros de réseau et
	d’hôte et l’adresse de broadcast pour IP=193.54.193.12.

4. \
	Donnez le masque réseau et son /n puis les numéros de réseau et
	d’hôte et l’adresse de broadcast pour IP=225.67.127.30.

5. \
	Donnez le nombre d’hôtes du réseau IP=8.8.8.8 et
	MR=255.255.255.192

6. \
	Donnez le nombre d’hôtes du réseau IP=8.8.8.8/22.

7. \
	J’ai à disposition le réseau 192.168.5.64/28, je désire faire 3 sous réseaux
	de 6, 4 et 3 hôtes. Est-ce possible?

8. \
	J’ai à disposition le réseau 192.168.5.64/27, je désire faire 3 sous réseaux
	de 6, 4 et 3 hôtes. Donnez un découpage possible (IP/MR
	de chaque sous réseau).

.. toctree::
   :maxdepth: 1

	Proposition de correction n°1			<cours/d4>

| :code:`[TAG] ENSIIE PWR CM1 2021 S2`

4. Maitre des protocoles
===================================

1. \
	L’établissement de la liaison de communication avec l’entité vis-à-vis
	est une phase complexe des protocoles.

2. \
	Un protocole de niveau N est défini indépendamment de la couche
	N-1 sur laquelle il s’appuie.

3. \
	Un protocole peut être implanté sur n’importe quel autre protocole
	qui s'appuie sur la couche N-1.

4. \
	Soit A et B, 2 mises en oeuvre d’une présentation API d’un protocole
	P, écrites par 2 personnes différentes. A et B peuvent elles communiquer ?

5. \
	Soit A une mise en oeuvre d’une présentation API1 d’un protocole
	P, et B une mise en oeuvre d’une présentation API2 d’un protocole
	P. A et B peuvent elles communiquer ?

6. \
	Dans l’automate qui spécifie le dialogue d’un protocole N apparait
	les services du protocole N-1.

7. \
 	La mise en oeuvre d’un protocole de niveau N utilise les services du
	protocole N-1.

8. \
	La mise en oeuvre d’un protocole de niveau N-1 appelle les services
	du protocole N.

9. \
	Un protocole peut-il ne pas avoir de service?

10. \
	Une entité d’un protocole peut-elle ne pas avoir de service?

.. toctree::
   :maxdepth: 1

	Proposition de correction n°1			<cours/d5>

| :code:`[TAG] ENSIIE PWR CM1 2021 S2`

Niveau supérieur
***********************

1. Exploration
------------------------------

La commande ping permet de préciser avec l'option -t la durée de vie (TTL : Time To Live)
du paquet ip correspondant. Ce paramètre représente le nombre maximal de routeurs de transit.
A chaque routeur traversé, le TTL est décrémenté. Lorsqu'il atteint la valeur 0, le paquet est détruit,
et un paquet ICMP (11 : Time exceeded) est envoyé à la source si le routeur est configuré pour cela
(ceci évite qu'un paquet boucle à l'infini s’il existe un problème de boucle de routage).

En utilisant la commande ping, et en incrémentant manuellement le ttl à chaque tentative,
donnez si possible tous les nœuds jusqu'aux machines (la commande ping ne devra pas
attendre plus d'une seconde)

	* www.archlinux.org
	* www.free.fr
	* www.google.fr
	* www.rien.org

On va automatiser la démarche pour découvrir l'ensemble des nœuds traversés jusqu'à une machine.

Écrire un script trace.sh qui prend en argument un nom/ip de machine,
et qui affiche les nœuds traversés. On utilise la même idée que précédemment:
la commande ping, et les options -c, -t, -W. Un exemple de la sortie attendue :

.. code:: bash

		./trace.sh www.archlinux.org
		1 : gatekeeper.arda (172.16.1.254)
		2 : 37.58.131.238 (37.58.131.238)
		3 : 100.65.0.27 (100.65.0.27)
		4 : c4-stg.e6-stg.backbone.adista.fr (128.127.131.113)
		5 : c4-stg.e6-stg.backbone.adista.fr (128.127.131.113)
		6 : decix-gw.hetzner.de (80.81.192.164)
		7 : core24.fsn1.hetzner.com (213.239.252.42)
		8 : ex9k2.dc8.fsn1.hetzner.com (213.239.229.22)
		9 : apollo.archlinux.org (138.201.81.199)

.. code:: bash

		./trace.sh www.free.fr
		1 : gatekeeper.arda (172.16.1.254)
		2 : 37.58.131.238 (37.58.131.238)
		3 : 100.65.0.27 (100.65.0.27)
		4 : c2-th2.t1-th2.backbone.adista.fr (128.127.131.185)
		5 : c2-th2.t1-th2.backbone.adista.fr (128.127.131.185)
		6 : cr2-adista.customers-th2.ielo.net (212.85.149.53)
		7 : no reply
		8 : no reply
		9 : no reply
		10 : no reply
		11 : bzn-9k-4-be1004.intf.routers.proxad.net (78.254.249.2)
		12 : no reply
		13 : bzn-9k-2.sys.routers.proxad.net (212.27.32.146)
		14 : www.free.fr (212.27.48.10)

| :code:`[TAG] IUTSF ASR TP1 2019 S2`

Niveau avancé
***********************

aucun

-----

**Crédits**
	* Selma NABOULSI (enseignants à l'IUT de Sénart-Fontainebleau)
	* Frédéric GERVAIS (enseignants à l'IUT de Sénart-Fontainebleau)
	* enseignant de l'ENSIIE du cours 2018-2019