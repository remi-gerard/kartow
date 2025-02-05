# Kartow

## Lancement du projet

Dans le répertoire Docker

Build des images db et kartow
```bash
docker-compose up --build
```

### Récupération et injection des données dans le conteneur db
```bash
docker ps
docker exec -u root -it xxxxxxxxx sh
wget https://lz4.overpass-api.de/api/xapi_meta?*[bbox=4.77,43.96,4.79,43.97] -O data.osm
su postgres
createuser osmuser
createdb --encoding=UTF8 --owner=osmuser osm
psql osm --command='CREATE EXTENSION postgis;';
psql osm --command='CREATE EXTENSION hstore;';
osm2pgsql -m -d osm data.osm
exit
rm -f data.osm
```

#### Création des conteneurs
```bash
docker build -t kartow .
docker build -t db .
```

L'argument -t permet de donner un nom à votre image Docker.
Le . est le répertoire où se trouve le Dockerfile

#### Lancement des conteneurs
```bash
docker run -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=postgres db
```

#### Se connecteur à un conteneur
```bash
docker ps
docker exec -u root -it c81438ad400f sh
```
