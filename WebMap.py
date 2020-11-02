def list_maker(makerobject):
    list = []
    for i in makerobject:
        list.append(i)
    return list

def elevtester(height):
    float(height)
    if height > 2000 and height < 3000:
        return 'orange'
    elif height > 3000:
        return 'red'
    else:
        return 'green'
import folium
import pandas
import json

dataframe = pandas.read_csv("Volcanoes.txt")
count = 0
latitude = list_maker(dataframe["LAT"])
longitude = list_maker(dataframe["LON"])
name = list_maker(dataframe["NAME"])
location = list_maker(dataframe["LOCATION"])
height = list_maker(dataframe["ELEV"])
html = """<h4>Volcano Information: </h4>
<h5>Location: %s</h5>
<h5>Height: %d </h5>
"""
iconobject = ''


map = folium.Map(location = [48.78,-121.81], zoom_start = 8, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name = "Volcano Map")
fp = folium.FeatureGroup(name = "Population Map")

while count != len(latitude):
    iconobject = elevtester(height[count])
    pop = folium.IFrame(html = html % (name[count] + ", " + location[count], height[count]), width = 200, height = 125)
    fg.add_child(folium.CircleMarker(location = [latitude[count],longitude[count]], radius = 6,
    popup = folium.Popup(pop), fill_color = iconobject, color = 'grey', fill_opacity = 0.7))
    count = count + 1

fp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red'}))


map.add_child(fg)
map.add_child(fp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
