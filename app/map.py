import folium
import requests

from folium.map import Icon

response = requests.get("http://localhost:3001/areas")
json = response.json()
datas = json["data"]

# response api
# datas = [
#     {"name": "ร้านต้นไม้มีชีวิต", "location": [13.120901, 100.919166]},
#     {"name": "ร้านรักโลก", "location": [12.4453, 99.98189]},
#     {"name": "ร้านเหนือต้นไม้คือท้องฟ้า", "location": [20.2778358878, 99.8697515215]},
# ]


map = folium.Map(location=[13.120901, 100.919166], zoom_start=6)

fg = folium.FeatureGroup("THAI MAP <3")
for data in datas:
    fg.add_child(
        folium.Marker(
            location=data["location"], popup=data["name"], icon=folium.Icon(color="red")
        )
    )

map.add_child(fg)
map.save("map.html")
