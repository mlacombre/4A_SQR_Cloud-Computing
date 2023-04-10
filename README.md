
# Flipper

Ce répertoire github, contient un projet scolaire qui vise à créer une copie de twitter afin de s'entrainer à la création d'API. 

Ce répertoire est composé de deux sous répertoire.


- Backend
- Frontend

## Backend

le backend de ce projet est composé d'un fichier python qui forme l'API grâce à Flask. 
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Cette API permet plusieurs opération détaillé dans le README du répertoire. 

## Frontend

Le Frontend à pour objectif de fournir un moyen de questionner l'API afin de reproduire un fonctionnemnt simplifier de twitter. Cependant il est encore en contruction et n'est pas fini à cause d'un problème avec les CORS.





## Authors

- [@gabinde](https://github.com/gabinde) gabin Deroues
- [@mlacombre](https://github.com/mlacombre) morgane Lacombre
## Tech Stack

**Client:** HTML, CSS, Javascript

**Server:** Flask, Redis


## Procédure

Pour déployer le server flask 

```bash
  docker build -t flask-image:v1 .
```

```bash
  docker run -d -p 5000:5000 flask-image:v1
```

Pour déployer la base de donnée Redis

```bash
    docker run --name myredis -p 6379:6379 redis
```

Pour déployer le Frontend 

```bash
    docker pull nginx
```
```bash
    docker build -t nginx-myapplication .
```

```bash
    docker run –name mycontainer-nginx -p 8052:80 -d nginx-myapplication
```

