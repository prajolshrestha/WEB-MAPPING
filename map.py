import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

########################################## Add base layer ###########################################
map =folium.Map(location=[38.58,-99.09],zoom_start=6, tiles="Stamen Terrain")   #here map is class 'folium.folium.Map'

#lets make popup message look lively
html = """<h4>Volcano Information:</h4>
<br><a href = "https://www.google.com/search?q=%%22%s%%22"
target="_blank">%s</a></br>
 Height:%s m"""       #add html in popup message

def color_generator(elevation):
    if elevation <= 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

##############################lets add elements , object of the maps, children of maps, or feature of maps##############################
#map.add_child(folium.Marker(location=[38.58,-99.2],popup="Hi, I am a marker", icon=folium.Icon(color="green")))

############################## add objects using for loop ##########################################
#fg = folium.FeatureGroup(name="My Map")
#for coordinate in [[38.1,-99],[37,-98]]:
#    fg.add_child(folium.Marker(location=coordinate,popup="I am a marker", icon=folium.Icon(color="green")))
#map.add_child(fg)


feature_group = folium.FeatureGroup(name="Volcanoes")   #Create a FeatureGroup layer ; you can put things in it and handle them as a single layer. 

################################ Easy and organized way to add marker layer #########################################
for lt,ln,el,name in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (name,name,el),width =200,height =100)
    #feature_group.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe), icon=folium.Icon(color=color_generator(el))))  #for normal icon
    feature_group.add_child(folium.CircleMarker(location=[lt,ln], radius= 6, popup=folium.Popup(iframe),  fill=True, fill_color=color_generator(el), color='grey', fill_opacity=0.7)) # for circular icon

################################ lets add polygen layer ################################
fg1 = folium.FeatureGroup(name="Population")
fg1.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 1000000
else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))             #create file object using open and add polygon and change color


map.add_child(feature_group)
map.add_child(fg1)
################################# lets add layer control ###################################
map.add_child(folium.LayerControl())

################################ Save map ################################
map.save("Map1.html")