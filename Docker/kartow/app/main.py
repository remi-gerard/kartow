import  mapnik
import cairo

from mapnik import Coord, Box2d


bbox = Box2d(530994,5459254,533220,5460801)

width = 1600
height = 1600

def generate_svg(style, output, width, height, bbox):
	map = mapnik.Map(width, height)
	mapnik.load_map(map, style)
	map.zoom_to_box(bbox)
	mapnik.render_to_file(map, output)

###################### LAYERS ######################

style_01 = './styles/01_roads_big.xml'
output_01 = './output/01_roads_big.svg'
generate_svg(style_01, output_01, width, height, bbox)

########################################################

style_02 = './styles/02_roads_middle.xml'
output_02 = './output/02_roads_middle.svg'
generate_svg(style_02, output_02, width, height, bbox)

########################################################

style_03 = './styles/03_roads_little.xml'
output_03 = './output/03_roads_little.svg'
generate_svg(style_03, output_03, width, height, bbox)

########################################################

style_04 = './styles/04_trains.xml'
output_04 = './output/04_trains.svg'
generate_svg(style_04, output_04, width, height, bbox)

########################################################

style_05 = './styles/05_planes.xml'
output_05 = '/home/rgerard/Desktop/output/05_planes.svg'
generate_svg(style_05, output_05, width, height, bbox)

########################################################

style_06 = './styles/06_buildings.xml'
output_06 = './output/06_buildings.svg'
generate_svg(style_06, output_06, width, height, bbox)

########################################################

style_07 = './styles/07_dark_green.xml'
output_07 = './output/07_dark_green.svg'
generate_svg(style_07, output_07, width, height, bbox)

########################################################

style_08 = './styles/08_tree_row.xml'
output_08 = './output/08_tree_row.svg'
generate_svg(style_08, output_08, width, height, bbox)

########################################################

style_09 = './styles/09_light_green.xml'
output_09 = './output/09_light_green.svg'
generate_svg(style_09, output_09, width, height, bbox)

########################################################

style_10 = './styles/10_beach.xml'
output_10 = './output/10_beach.svg'
generate_svg(style_10, output_10, width, height, bbox)

########################################################

style_11 = './styles/11_water_land.xml'
output_11 = './output/11_water_land.svg'
generate_svg(style_11, output_11, width, height, bbox)

########################################################

style_12 = './styles/12_bridge.xml'
output_12 = './output/12_bridge.svg'
generate_svg(style_12, output_12, width, height, bbox)

########################################################

style_13 = './styles/13_pavement.xml'
output_13 = './output/13_pavement.svg'
generate_svg(style_13, output_13, width, height, bbox)

########################################################

style_14 = './styles/14_river_big.xml'
output_14 = './output/14_river_big.svg'
generate_svg(style_14, output_14, width, height, bbox)

########################################################

style_15 = './styles/15_river_little.xml'
output_15 = './output/15_river_little.svg'
generate_svg(style_15, output_15, width, height, bbox)

########################################################

style_16 = './styles/16_water.xml'
output_16 = './output/16_water.svg'
generate_svg(style_16, output_16, width, height, bbox)

########################################################

style_17 = './styles/17_full_buildings.xml'
output_17 = './output/17_full_buildings.svg'
generate_svg(style_17, output_17, width, height, bbox)

########################################################

style_18 = './styles/18_roads_name.xml'
output_18 = './output/18_roads_name.svg'
generate_svg(style_18, output_18, width, height, bbox)

########################################################

style_99 = './styles/99_roads_forgot.xml'
output_99 = './output/99_roads_forgot.svg'
generate_svg(style_99, output_99, width, height, bbox)

##################### SAMPLE #####################

output = './output/sample.png'
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

print('#### Generation completed ####')
