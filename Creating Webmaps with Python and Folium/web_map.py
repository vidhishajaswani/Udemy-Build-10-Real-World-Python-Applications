# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 00:46:29 2018

@author: Vidhisha
"""

import folium
import pandas

#read lat and long from txt file
data=pandas.read_csv("Volcanoes_USA.txt")
lat=list(data['LAT'])
lon=list(data['LON'])
ele=list(data["ELEV"])

#function to return diff colors for diff elevations
def get_color(elevation):
    if elevation<1000:
        return 'green'
    elif 1000 <= elevation<3000:
        return 'blue'
    else:
        return 'red'

#build the map
map=folium.Map(location=[38,-99],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Volcanoes")
for lt,ln,e in zip(lat,lon,ele):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6,popup=str(e)+" m",
                                     fill_color=get_color(e),color='grey',fill_opacity=0.7,fill=True))
map.add_child(fgv)

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")