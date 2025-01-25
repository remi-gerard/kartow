import  mapnik
import cairo

from mapnik import Coord, Box2d

# Le Pontet : wget https://lz4.overpass-api.de/api/xapi_meta?*[bbox=4.82,43.94,4.9,43.99] -O data.osm / Projection 536560 5456162 545466 5463895
# Le Pontet Mieux cadré : https://lz4.overpass-api.de/api/xapi_meta?*[bbox=4.82,43.94,4.9,44.01] -O / Projection 536560 5456162 545466 5466990
# Le Pontet LinkedIn : wget https://lz4.overpass-api.de/api/xapi_meta?*[bbox=4.7,43.94,5.03,44.01] -O data.osm
# Projection 523202 5456162 559937 5466990
# Avignon : wget https://lz4.overpass-api.de/api/xapi_meta?*[bbox=4.7843.92,4.86,43.96] -O data.osm / Projection 532107 5453070 541013 5459254

# Stockholm : wget https://lz4.overpass-api.de/api/xapi_meta?*[bbox=17.96,59.24,18.18,59.39] -O data.osm / Projection 1999298 8232442 2023788 8265163


# sudo -u postgres -i
# osm2pgsql -m -d gis /home/rgerard/Desktop/osm/data.osm
bbox = Box2d(1999298,8232442,2023788,8265163)

width = 1600
height = 1600

def generate_svg(style, output, width, height, bbox):
	map = mapnik.Map(width, height)
	mapnik.load_map(map, style)
	map.zoom_to_box(bbox)
	mapnik.render_to_file(map, output)

###################### LAYERS ######################

style_01 = './styles/01_roads_big.xml'
output_01 = '/home/rgerard/Desktop/output/01_roads_big.svg'
generate_svg(style_01, output_01, width, height, bbox)

########################################################

style_02 = './styles/02_roads_middle.xml'
output_02 = '/home/rgerard/Desktop/output/02_roads_middle.svg'
generate_svg(style_02, output_02, width, height, bbox)

########################################################

style_03 = './styles/03_roads_little.xml'
output_03 = '/home/rgerard/Desktop/output/03_roads_little.svg'
generate_svg(style_03, output_03, width, height, bbox)

########################################################

style_04 = './styles/04_trains.xml'
output_04 = '/home/rgerard/Desktop/output/04_trains.svg'
generate_svg(style_04, output_04, width, height, bbox)

########################################################

style_05 = './styles/05_planes.xml'
output_05 = '/home/rgerard/Desktop/output/05_planes.svg'
generate_svg(style_05, output_05, width, height, bbox)

########################################################

style_06 = './styles/06_buildings.xml'
output_06 = '/home/rgerard/Desktop/output/06_buildings.svg'
generate_svg(style_06, output_06, width, height, bbox)

########################################################

style_07 = './styles/07_dark_green.xml'
output_07 = '/home/rgerard/Desktop/output/07_dark_green.svg'
generate_svg(style_07, output_07, width, height, bbox)

########################################################

style_08 = './styles/08_tree_row.xml'
output_08 = '/home/rgerard/Desktop/output/08_tree_row.svg'
generate_svg(style_08, output_08, width, height, bbox)

########################################################

style_09 = './styles/09_light_green.xml'
output_09 = '/home/rgerard/Desktop/output/09_light_green.svg'
generate_svg(style_09, output_09, width, height, bbox)

########################################################

style_10 = './styles/10_beach.xml'
output_10 = '/home/rgerard/Desktop/output/10_beach.svg'
generate_svg(style_10, output_10, width, height, bbox)

########################################################

style_11 = './styles/11_water_land.xml'
output_11 = '/home/rgerard/Desktop/output/11_water_land.svg'
generate_svg(style_11, output_11, width, height, bbox)

########################################################

style_12 = './styles/12_bridge.xml'
output_12 = '/home/rgerard/Desktop/output/12_bridge.svg'
generate_svg(style_12, output_12, width, height, bbox)

########################################################

style_13 = './styles/13_pavement.xml'
output_13 = '/home/rgerard/Desktop/output/13_pavement.svg'
generate_svg(style_13, output_13, width, height, bbox)

########################################################

style_14 = './styles/14_river_big.xml'
output_14 = '/home/rgerard/Desktop/output/14_river_big.svg'
generate_svg(style_14, output_14, width, height, bbox)

########################################################

style_15 = './styles/15_river_little.xml'
output_15 = '/home/rgerard/Desktop/output/15_river_little.svg'
generate_svg(style_15, output_15, width, height, bbox)

########################################################

style_16 = './styles/16_water.xml'
output_16 = '/home/rgerard/Desktop/output/16_water.svg'
generate_svg(style_16, output_16, width, height, bbox)

########################################################

style_17 = './styles/17_full_buildings.xml'
output_17 = '/home/rgerard/Desktop/output/17_full_buildings.svg'
generate_svg(style_17, output_17, width, height, bbox)

########################################################

style_18 = './styles/18_roads_name.xml'
output_18 = '/home/rgerard/Desktop/output/18_roads_name.svg'
generate_svg(style_18, output_18, width, height, bbox)

########################################################

style_99 = './styles/99_roads_forgot.xml'
output_99 = '/home/rgerard/Desktop/output/99_roads_forgot.svg'
generate_svg(style_99, output_99, width, height, bbox)

##################### SAMPLE ##################### 

output = '/home/rgerard/Desktop/output/sample.png'
map = mapnik.Map(width, height)
mapnik.load_map(map, style_01)
mapnik.load_map(map, style_02)
mapnik.load_map(map, style_03)
mapnik.load_map(map, style_04)
mapnik.load_map(map, style_05)
mapnik.load_map(map, style_07)
mapnik.load_map(map, style_08)
mapnik.load_map(map, style_09)
mapnik.load_map(map, style_10)
mapnik.load_map(map, style_11)
mapnik.load_map(map, style_12)
mapnik.load_map(map, style_13)
mapnik.load_map(map, style_14)
mapnik.load_map(map, style_15)
mapnik.load_map(map, style_16)
mapnik.load_map(map, style_17)
mapnik.load_map(map, style_06)
mapnik.load_map(map, style_18)

map.zoom_to_box(bbox)
mapnik.render_to_file(map, output)

