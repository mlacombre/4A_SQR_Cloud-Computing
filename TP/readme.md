
# API FLIPPER

Dans ce répertoire, vous trouverez tous les dossiers correspondants au backend de FLIPPER. Vous trouverez : un fichier pour dockeriser ainsi que l'API


## Techno API

**Server:** FLASK

**BDD:** REDIS


## REDIS

L'ensemble des informations sont stocké dans des bases redis. Pour installer redis avant installation, il faut utiliser : 

```bash
docker run --name myredis -p 6379:6379 redis
```

Dans cette API, deux bases redis différentes sont utilisées. La première : rUsername stockera les informations comme suit : 

````bash 
key=timestamp, value=’{“author”: “username”, “flip”: ”message”}’
`````
La clé est ici le timestamp d'un flip.

Cependant dans le cas d'un retweet, il sera possible de modifier la value pour ajouter une clé reflipper dans le dictionnaire ce qui ressemblera à: 

````bash 
key=timestamp, value=’{“author”: “username”, “flip”: ”message”, "reflipper": "reflipper}’
`````

La seconde base, servira à stocker à la fois les auteurs et les timestamps de leur tweets ainsi que les sujets et les timestamps des moments où ils aapparaissent. On stockera les informations comme suit : 
````bash 
key= "u-"+author, value=[timestamp_1, timestamp_2, timestamp_3]
`````
````bash 
key="h-"+hashtag, value=[timestamp_1, timestamp_2, timestamp_3]
`````

Les préfixes "u-" et h-" assurent qu'aucun sujets ne peut correspondrent à un auteur


## ROUTES

cette API dispose de 6 routes :


#### Flip

```bash
  POST /flip/<author>/<flip>
```

cette route permet de stocker un flip dans deux bases redis comme préciser ci-desssus.

Elle permet aussi de stocker lmes sujets grâce à l'expression régulière : 

`r"(?<!\w)#[A-Za-z0-9]+(?![A-Za-z0-9]*#)"`

##### Attention ⚠️, la regex ne prend pas les accents en compte

#### Récupération de l'ensemble des Flips

```bash
  GET /getAllFlip
```

Cette route permet de récupérer l'ensemble des flips qui ont été écrits.

#### Récupération de l'ensemble des Flips d'un utilisateur

```bash
  GET /getFlipByUser/<User>
```

Cette route permet de récupérer l'ensemble des flips qu'un utilisateur à écrits ou reflippé.

#### Récupération de l'ensemble des sujets

```bash
  GET /getAllSubject
```
Cette route récupère l'ensemble des sujets stocké dans la base reddis. 


#### Récupération de l'ensemble des flips ou apparait un sujet

```bash
  GET /getFlipByHashtag/<sujet>
````

celle ci permet de récupérer l'ensemble des flips ou apparait un sujet.

#### Reflip

```bash
  POST /Reflip/<flipper>/<reflipper>/<reflipped>
````

Cette route permet de stocker en base de donnée un nouveau tweet équivalent à celui tweeté cependant rajoute une donnée reflipper dans le tweet permettant de savoir que le tweet est un retweet et qui la retweet
##### Attention ⚠️, il est possible de reflipper plusieurs fois un même flip avec cette méthode. Aucun mécanisme n'a été rajouté pour l'empécher.
