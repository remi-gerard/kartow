#!/bin/sh

wget https://lz4.overpass-api.de/api/xapi_meta?*[bbox=4.77,43.96,4.79,43.97] -O data.osm
su postgres
createuser osmuser
createdb --encoding=UTF8 --owner=osmuser osm
psql osm --command='CREATE EXTENSION postgis;';
psql osm --command='CREATE EXTENSION hstore;';
osm2pgsql -m -d osm data.osm
exit
rm -f data.osm
