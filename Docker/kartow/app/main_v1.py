import  mapnik
from mapnik import Coord, Box2d

# Le Pontet : wget https://lz4.overpass-api.de/api/xapi_meta?*[bbox=4.82,43.94,4.9,43.99] -O data.osm / Projection 536560 5456162 545466 5463895
# sudo -u postgres -i
# osm2pgsql -m -d gis /home/rgerard/Desktop/osm/data.osm


style = 'style.xml'
output = 'output.png'

width = 800
height = 800

bbox = Box2d(536560,5456162,545466,5463895)

map = mapnik.Map(width, height)
mapnik.load_map(map, style)

map.zoom_to_box(bbox)
mapnik.render_to_file(map, output)
