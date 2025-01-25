import  mapnik

map = mapnik.Map (600 ,300)
map.background = mapnik.Color('steelblue')

polygons = mapnik.PolygonSymbolizer ()
polygons.fill = mapnik.Color('lightgreen')

rules = mapnik.Rule()
rules.symbols.append(polygons)

style = mapnik.Style()
style.rules.append(rules)
map.append_style('Countries', style)

layer = mapnik.Layer('world')
layer.datasource = mapnik.Shapefile(file='/home/rgerard/Desktop/shp/countries/CNTR_BN_01M_2020_3035.shp')
layer.styles.append('Countries')

map.layers.append(layer)
map.zoom_all ()
mapnik.render_to_file(map , '/home/rgerard/Desktop/output/world.svg', 'svg')
