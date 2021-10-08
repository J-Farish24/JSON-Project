#Import statements
from io import TextIOBase
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
#Opens json file and creates a json object
FILE = 'US_fires_9_1.json'
infile = open(FILE)
fire_list = json.load(infile)
infile.close()
#List comprehensions to create lists for lats, lons, and brightness
#Only adds fire if brightness is greater than 450
latitudes = [fire['latitude'] for fire in fire_list if fire['brightness'] > 450]
longitudes = [fire['longitude'] for fire in fire_list if fire['brightness'] > 450]
brightnesses = [fire['brightness'] for fire in fire_list if fire['brightness'] > 450]
#Create data list for graph
data = [
    {
        "type": "scattergeo",
        "lon": longitudes,
        "lat": latitudes,
        "text": brightnesses,
        "marker": {
            "color": brightnesses,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]
#Create graph
my_layout = Layout(title="US Fires - 9/1/2020 Through 9/13/2020")
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="us_fires_from_sep1-sep13.html")
