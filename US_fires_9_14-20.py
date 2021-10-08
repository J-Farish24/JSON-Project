#Imports
from io import TextIOBase
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
#Open file and create json object so I can access the dictionaries in the list
FILE = 'US_fires_9_14.json'
infile = open(FILE, 'r')
fires_list = json.load(infile)
#Create lats lons and brightnesses lists using list comprehension
brightnesses = [fire['brightness'] for fire in fires_list if fire['brightness'] > 450]
lats = [fire['latitude'] for fire in fires_list if fire['brightness'] > 450]
lons = [fire['longitude'] for fire in fires_list if fire['brightness'] > 450]
#Create data list for graph
data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": brightnesses,
        "marker": {
            #Make marker size the same for each fire and more visible
            "size": [20 for fire in brightnesses],
            "color": brightnesses,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]
#Create graph 
#geo_scope limits the scope of the map to the United States
my_layout = Layout(title="US Fires - 9/14/2020 Through 9/20/2020", geo_scope = 'usa')
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="us_fires_from_sep14-sep20.html")
