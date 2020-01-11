import folium
import pandas


maps = folium.Map(location=[18,-69], zoom_start=6)

# fg.add_child(folium.Marker(location = [18,-69],popup="Hola",icon=folium.Icon(color='green')))
# # anade multiple coordenadas
# for coordinate in [[18.5,-68],[17.9,-69],[18.9,-69.5]]:
#     fg.add_child(folium.Marker(location = coordinate,popup="Hola",icon=folium.Icon(color='green')))

data =  pandas.read_csv("Volcanoes.txt")

coordLat = list(data["LAT"]) 
coordLon = list(data["LON"]) 
coordEle = list(data["ELEV"])
CoordName = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://en.wikipedia.org/wiki/%s" target="_blank">%s</a><br>
Height: %s m
"""
def colorelevation(elevetion):
    if elevetion < 1000:
        return "green"
    elif 1000<= elevetion >=3000:
        return "orange"
    else:
        return "red"

fgv =  folium.FeatureGroup(name="Volcanos")

for lat, lon, ele,name in zip(coordLat,coordLon, coordEle, CoordName):
    frame = folium.IFrame(html=html % (name, name, ele), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location = [lat,lon],radius=6, popup=folium.Popup(frame),fill_color= colorelevation(ele),color='grey',fill_opacity=7))

fgp =  folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read() ),style_function= lambda x: {'fillColor' : 'yellow' if x['properties'] ['POP2005'] 
< 10000000 else 'green' if 10000000 <= x['properties'] ['POP2005'] < 100000000 else 'red'}))

maps.control_scale = True
maps.add_child(fgv)
maps.add_child(fgp)
maps.add_child(folium.LayerControl())


maps.save("Map1.html")