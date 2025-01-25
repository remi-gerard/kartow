# Kartow

## Docker

### db

#### Récupération des données
```bash
docker exec -u root -it xxxxxxxxx sh
wget https://lz4.overpass-api.de/api/xapi_meta?*[bbox=17.96,59.24,18.18,59.39] -O data.osm
exit
```
#### Injection des données
```bash
docker exec -u postgres -it xxxxxxxxx sh
createuser osmuser
psql -U postgres
createdb --encoding=UTF8 --owner=osmuser osm
exit
psql osm --command='CREATE EXTENSION postgis;';
psql osm --command='CREATE EXTENSION hstore;';
osm2pgsql -m -d osm data.osm
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
