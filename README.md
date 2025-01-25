# Kartow

## Docker

### Création des conteneurs
```bash
docker build -t kartow .
docker build -t db .
```

L'argument -t permet de donner un nom à votre image Docker.
Le . est le répertoire où se trouve le Dockerfile

### Lancement des conteneurs
```bash
docker run -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=postgres db
```

### Se connecteur à un conteneur
```bash
docker ps
docker exec -it c81438ad400f sh
```
